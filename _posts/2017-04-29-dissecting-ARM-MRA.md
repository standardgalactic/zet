---
layout: post
title: Dissecting ARM's Machine Readable Specification
---

Last week, ARM released their Machine Readable
Architecture Specification and
[I wrote about what you can do with it]({{ site.baseurl
}}{% post_url 2017-04-20-ARM-v8a-xml-release %}).
But before you can do anything with the specification, you need
to extract the useful bits from the release so I thought I would try
for myself and describe what I found out (and [release some
scripts](https://github.com/alastairreid/mra_tools) that demonstrate/test
what I am saying).

So what exactly is in the release?

* It contains a lot of html files (see [Milosch Meriac's online v8-A html](https://www.meriac.com/archex/A64_v82A_ISA/))

      $ tar ztf A64_v82A_ISA_xml_00bet3.1.tar.gz | grep xhtml
      ISA_v82A_A64_xml_00bet3.1/xhtml/
      ISA_v82A_A64_xml_00bet3.1/xhtml/rev.html
      ISA_v82A_A64_xml_00bet3.1/xhtml/sabd_advsimd.html
      ISA_v82A_A64_xml_00bet3.1/xhtml/smlal_advsimd_vec.html
      ISA_v82A_A64_xml_00bet3.1/xhtml/rev16_int.html
      ISA_v82A_A64_xml_00bet3.1/xhtml/dup_advsimd_gen.html
      ISA_v82A_A64_xml_00bet3.1/xhtml/ushl_advsimd.html
      ISA_v82A_A64_xml_00bet3.1/xhtml/staddb.html
      ISA_v82A_A64_xml_00bet3.1/xhtml/orr_advsimd_imm.html
      ... 1300 more files omitted

    These are the human readable version of the specification --- all nicely
    hyperlinked.  This is the best way to navigate the ARM specification.

* It contains some pdf files

      $ tar ztf A64_v82A_ISA_xml_00bet3.1.tar.gz | grep pdf
      ISA_v82A_A64_xml_00bet3.1.pdf
      ISA_v82A_A64_xml_00bet3.1_OPT.pdf
      ISA_v82A_A64_xml_00bet3.1_OPT_diff.pdf

  These contain the same information as the html files above.
  The "OPT" versions are equivalent to the standard version but they have
  had some simplifying optimisations applied to make them more readable.
  The "OPT_diff" versions show the difference between the standard version
  and the OPT version --- the best way of understanding what the OPT version
  does.

* It contains some xml files

      $ tar ztf A64_v82A_ISA_xml_00bet3.1.tar.gz | grep xml
      ISA_v82A_A64_xml_00bet3.1/
      ISA_v82A_A64_xml_00bet3.1/fcvtps_float.xml
      ISA_v82A_A64_xml_00bet3.1/sbfiz_sbfm.xml
      ISA_v82A_A64_xml_00bet3.1/ld3_advsimd_mult.xml
      ISA_v82A_A64_xml_00bet3.1/fcvtpu_advsimd.xml
      ISA_v82A_A64_xml_00bet3.1/sqshl_advsimd_imm.xml
      ISA_v82A_A64_xml_00bet3.1/fmaxnm_advsimd.xml
      ISA_v82A_A64_xml_00bet3.1/umax_advsimd.xml
      ISA_v82A_A64_xml_00bet3.1/versions.txt
      ... 3000 more files omitted

  This is the bit that we want!
  There are two files of particular interest:

    * [notice.xml](https://www.meriac.com/archex/A64_v82A_ISA/notice.xml) ARM's
      legal notice
    * [shared_pseudocode.xml](https://www.meriac.com/archex/A64_v82A_ISA/shared_pseudocode.xml)
      hundreds of shared support functions used in the definition of instructions,
      page table walk, permission checking, exceptions/interrupts, etc.

  And the rest of the files are instruction encodings such as
  [adc.xml](https://www.meriac.com/archex/A64_v82A_ISA/adc.xml).

* And it contains files like a DTD file that defines the XML schema used by
  the XML.


## Inside the Shared XML files

The Shared XML files contain all the type definitions, constants, variables
and functions required by the instructions and system support code.
Here is how a typical function is presented in XML:

    <ps name="aarch32/debug/breakpoint/AArch32.BreakpointMatch"
        mylink="aarch32.debug.breakpoint.AArch32.BreakpointMatch"
        enclabels=""
        sections="1"
        secttype="Library">
       <pstext mayhavelinks="1"
               section="Functions"
               rep_section="functions">
           // AArch32.BreakpointMatch()
           // =========================
           // Breakpoint matching in an AArch32 translation regime.

           (boolean,boolean) <anchor link="AArch32.BreakpointMatch.3" hover="...">AArch32.BreakpointMatch</anchor>(integer n, bits(32) vaddress, integer size)
               assert <a link="impl-shared.ELUsingAArch32.1" file="shared_pseudocode.xml" hover="...">ELUsingAArch32</a>();
               ... more code
       </pstext>
    </ps>

This shows a named "ps" section containing a small number of related definitions
(just one in this case) and with the ASL implementation of the function
enclosed in a "pstext" section.
Almost all objects defined in the pstext section are tagged with "anchor"
and almost all references to objects in the pstext section are tagged with
"a".  (We will use these links later.)
The rest of the XML attributes are mostly useful for generating HTML --- I will
ignore them.

As we process this ASL code, it will be useful to track what definitions
each "ps" section contains and what the section depends on.
Here is a Python class to represent this (the full code is [here](https://github.com/alastairreid/mra_tools/blob/master/bin/instrs2asl.py)).

    class ASL:
        '''Representation of ASL code consisting of the code, list of names it defines and list of dependencies'''

        def __init__(self, name, code, defs, deps):
            self.name = name
            self.code = code
            self.defs = defs
            self.deps = deps

        def __str__(self):
            return "ASL{"+", ".join([self.name, str(self.defs), str(self.deps)])+"}"

and here is some code to read the XML, extract dependencies and package it up as
an ASL object.

    '''
    Read pseudocode to extract ASL.
    '''
    def readASL(ps):
        name = ps.attrib["name"]
        name = name.replace(".txt","")
        name = name.replace("/instrs","")
        name = name.replace("/Op_","/")
        chunk = ps.find("pstext")

        # list of things defined in this chunk
        defs = { x.attrib['link'] for x in chunk.findall('anchor') }

        # extract dependencies from hyperlinks in the XML
        deps = { x.attrib['link'] for x in chunk.findall('a') if not x.text.startswith("SEE") }

        # drop impl- prefixes in links
        deps = { re.sub('(impl-\w+\.)','',x) for x in deps }
        defs = { re.sub('(impl-\w+\.)','',x) for x in defs }

        # drop file references in links
        deps = { re.sub('([^#]+#)','',x) for x in deps }

        return ASL(name, ET.tostring(chunk, method="text").decode().rstrip()+"\n", defs, deps)


    '''
    Read shared pseudocode files to extract ASL.
    '''
    def readShared(files):
        asl = {}
        for f in files:
            xml = ET.parse(f)
            for ps in xml.findall('.//ps_section/ps'):
                r = readASL(ps)
                # Various workarounds omitted - see github repo
                asl[r.name] = r
        return asl

## Inside the Instruction XML files

The ARM architecture often contains several different encodings for a single instruction.
Each instruction shares some common ASL code to execute the instruction and (optionally) to
perform part of the decoding.
The "pstext" sections containing these are labelled "Execute" and "Postdecode".
Some instructions are just aliases for other instructions so they don't contain
an execute section --- I will discard these instructions.

    def readInstruction(xml):
        execs = xml.findall(".//pstext[@section='Execute']/..")
        posts = xml.findall(".//pstext[@section='Postdecode']/..")
        assert(len(posts) <= 1)
        assert(len(execs) <= 1)
        if not execs: return None # discard aliases

        exec = readASL(execs[0])
        post = readASL(posts[0]) if posts else None

These pieces of ASL can be shared by several different instruction encodings and each encoding
is accompanied by a piece of ASL to interpret the fields of the encoding.

        # for each encoding, read instructions encoding, matching decode ASL and index
        encs = []
        for iclass in xml.findall('.//classes/iclass'):

Instruction encodings and register descriptions use a common section format called "regdiagram".
One of the key pieces  of information about an instruction is which instruction set it belongs to.
The XML uses four different tags: "T16" (Thumb-32 short encoding), "T32" (Thumb-32 long encoding), "A32"
(ARM-32 encoding) and "A64" (ARM-64 encoding).  The T16 encoding is 16-bits long and all the others are 32-bits long.

            encoding = iclass.find('regdiagram')
            isT16 = encoding.attrib['form'] == "16"
            insn_set = "T16" if isT16 else iclass.attrib['isa']

The "regdiagram" section contains a number of boxes corresponding to one or more
contiguous bits within the encoding.
The location of each box is specified by
the width of the box and the highest bit position in the box.
Awkwardly, the T16 encoding numbers its bits from 31 down to 16
instead of from 15 down to 0 so my script fixes that.

            fields = []
            for b in encoding.findall('box'):
                wd = int(b.attrib.get('width','1'))
                hi = int(b.attrib['hibit'])
                # normalise T16 encoding bit numbers
                if isT16: hi = hi-16
                lo = hi - wd + 1

Some boxes have an attribute 'name', I use "_" for any anonymous boxes.

                nm  = b.attrib.get('name', '_')

And some boxes have a constant bitvector made up of "0", "1", "x", "(0)" or "(1)".
0 and 1 should be obvious, x means "don't care" and (0) and (1) mean
"should be 0/1 and it is UNPREDICTABLE what happens if they are not."
I use a suitable number of "x"s for any field with no constant specified.

The constant can also take the form "!= 1111" meaning "must not equal 1111".
This check is always replicated in the ASL code so I discard that information for now.

                consts = ''.join([ c.text for c in b.findall('c') if c.text is not None ])

                # normalise constants: note that it discards != information
                # because it is better obtained elsewhere in spec
                if consts == "" or consts.startswith('!='):
                    consts = 'x'*wd

Sometimes the XML splits a single field into two adjacent fields: typically one of the fields
has a constant value.
When this happens, the fields have a name like "reg<4:1>" and "reg<0>".
This is not very convenient for our purposes so I look for this pattern and
merge them back into a single field called "reg".

                # if adjacent entries are two parts of same field, join them
                # e.g., imm8<7:1> and imm8<0>
                m = re.match('^(\w+)<', nm)
                if m:
                    nm = m.group(1)
                    split = True
                    if fields[-1][3] and fields[-1][2] == nm:
                        (hi1,lo1,_,_,c1) = fields.pop()
                        assert(lo1 == hi+1) # must be adjacent
                        hi = hi1
                        consts = c1+consts
                else:
                    split = False

                fields.append((hi,lo,nm,split,consts))

To finish off reading an encoding, we
read the decode ASL and pick a good name for the instruction encoding.

            dec_asl = readASL(iclass.find('ps_section/ps'))

            name = dec_asl.name if insn_set in ["T16","T32","A32"] else encoding.attrib['psname']
            encs.append((name, insn_set, fields, dec_asl))

Finally, the collection of the encodings, the postdecode ASL and the execute ASL
are packaged up as an instruction named after the shared execute ASL.

        return Instruction(exec.name, encs, post, exec)

And to read all the instructions in a directory, we use the following code:

    instrs = []
    for d in args.dir:
        for inf in glob.glob(os.path.join(d, '*.xml')):
            name = re.search('.*/(\S+).xml',inf).group(1)
            if name == "onebigfile": continue
            xml = ET.parse(inf)
            instr = readInstruction(xml)
            if instr is None: continue
            instrs.append(instr)

## Sorting the shared code

Once you have extracted all the code, you are going to want to process it in some
way.
This will probably be easier to do if we arrange the ASL type and function definitions
so that definitions always occur before their first use.
So my script uses the dependencies that we extracted from the ASL to perform a
topological sort of the code.

There are several modes it can work in:

* Sort all the code.
  This will include code used by instructions but also code used when an interrupt
  occurs or an external debugger is attached.
* Extract all the code that is used by AArch64 instructions.  That is, instructions
  using the A64 encodings.
* Extract all the code that is used by AArch32 instructions.  That is, instructions
  using the A32 encodings.
* Extract all the code used by AArch64 or AArch32 instructions.

## Conclusion

I hope this is useful for those who want to make use of ARM's Machine Readable
Architecture specification.  The files are designed to meet many different
purposes so it is not always obvious which parts of them are useful for your
purpose.  This is why I thought it would be a good idea to write some scripts
that actually extract the code instead of just writing about how I believe you
can do it.

At work, I have access to the raw files  from which the XML files are built so it has
been a while since I have tried to extract the specification from the XML and it has been
interesting seeing how much easier it is to use the XML files than it was when I first
started using the architecture specs.
(But there were some issues that I had to work around as well --- search the script for the
word "workaround" for details.)

I would really welcome contributions from other people:

* I have a fairly narrow focus in what I want to do with the XML so my tools discard potentially useful information.
* I am also not a native Python speaker --- you can probably tell.
* Many of the people who want to use the machine readable specification
  are much more comfortable with functional languages --- translations are most welcome.

So if you have a suggestion for improving the scripts or you want other scripts, feel
free to implement your suggestion and send me a pull request.


Enjoy!

------

p.s., unpacking the tarballs and extracting the code is just the beginning.
I am working with
[Cambridge University's REMS research group](https://www.cl.cam.ac.uk/~pes20/rems/)
to convert the ASL to their SAIL language from which you can generate O'Caml, LEM
and HOL versions of the spec (with more backends planned).

And if the SAIL version does not suit your needs, then you might want want to
know how to lex, parse, typecheck and execute ASL code yourself.  I will
describe those in future posts.

### Related posts and papers

* Paper: [End-to-End Verification of ARM Processors with ISA-Formal]({{ site.url }}/papers/cav2016_isa_formal.pdf), CAV 2016.
* [Verifying against the official ARM specification]({{ site.baseurl }}{% post_url 2016-07-26-using-armarm %})
* [Finding Bugs versus Proving Absence of Bugs]({{ site.baseurl }}{% post_url 2016-07-18-finding-bugs %})
* [Limitations of ISA-Formal]({{ site.baseurl }}{% post_url 2016-07-30-isa-formal-limitations %})
* Paper: [Trustworthy Specifications of ARM v8-A and v8-M System Level Architecture]({{ site.url }}/papers/fmcad2016-trustworthy.pdf)), FMCAD 2016.
* [ARM's ASL Specification Language]({{ site.baseurl }}{% post_url 2016-08-17-specification_languages %})
* [ARM Releases Machine Readable Architecture Specification]({{ site.baseurl }}{% post_url 2017-04-20-ARM-v8a-xml-release %})
* This post: [Dissecting the ARM Machine Readable Architecture files]({{ site.baseurl }}{% post_url 2017-04-29-dissecting-ARM-MRA %})
* Code: [MRA Tools](https://github.com/alastairreid/mra_tools)
* [ASL Lexical Syntax]({{ site.baseurl }}{% post_url 2017-05-07-asl-lexical-syntax %})
* [Arm v8.3 Machine Readable Specifications]({{ site.baseurl }}{% post_url 2017-07-31-arm-v8_3 %})
* Paper: [Who guards the guards?  Formal Validation of the Arm v8-M Architecture Specification]({{ site.url }}/papers/oopsla2017-whoguardstheguards.pdf)), OOPSLA 2017.
* [Are Natural Language Specifications Useful?]({{ site.baseurl }}{% post_url 2017-08-19-natural-specs %})
* [Formal validation of the Arm v8-M specification]({{ site.baseurl }}{% post_url 2017-09-24-validating-specs %})
