---
title: What can you do with an ISA specification?
layout: post
---

ISA specifications describe the behaviour of a processor: the instructions,
memory protection, the privilege mechanisms, debug mechanisms, etc.
The traditional form of an ISA specification is as a paper document but,
as ISAs have grown, this has become unwieldy.
More importantly though, there are more and more
potential uses for machine readable, mechanized, executable ISA specifications.


## Documentation

The most obvious purpose of an ISA specification is as documentation.
An early formal notation is 
Bell and Newell's "Instruction Set Processor" (ISP) notation [[bell:afips:1970]]
that was used to write specifications for 14 systems including the PDP-8, PDP-11 and CDC 6600.
ISP followed in the Algol language tradition and is similar
to the less formal pseudocode notations typically used in ISA definitions in
the present day.
ISP was used during design of the PDP-11 and
included in the manufacturer's processor handbook [[pdp11:book:1973]].

Here is a fragment of a specification of the CDC 6600
[[bell:afips:1970]]
that shows how it compactly
describes assembly syntax, instruction encoding and semantics.

![CDC 600 specification]({{site.baseurl}}/images/CDC_6600_ISP.png "CDC 600 specification in ISP")

An even earlier ISA specification was Falkoff et al.'s
use of APL to describe the IBM System/360 [[falkoff:ibm:1964]].
However, given the novelty and unfamiliarity of APL at the time, it is not clear that the
primary goal was documentation.

![System/360 specification]({{site.baseurl}}/images/IBM_360_APL.jpg "System/360 specification in APL")


## Architecture design

Although it is common for ISA specifications to be written or updated *after*
the architecture has been designed or extended, a complete executable
specification can be a useful aid to architects as they are developing or
extending an architecture both by providing a clearer language (than natural
language) for expressing their thoughts and by allowing architects to test that
the changes behave as intended.

In addition,
having the architects themselves write and test the changes to
the specification
simplifies the process of developing and maintaining ISA
specifications and
avoids the effort and errors associated with transcribing
natural language documents and / or C++ simulators into some specification
language.

### Generating simulators

Shi's Simlight simulator[[shi:phd:2013], [joloboff:dsetta:2015]],
was based on parsing Arm's reference
manuals, Fox's MIPS specification [[fox:itps:2015]] written in L3 has been
shown to boot FreeBSD, and my own work within Arm [[reid:fmcad:2016]] was later
shown to be able to boot Linux.
An especially interesting approach is the  automatic generation of binary translations between architectures [[bansal:osdi:2008]].

Simulators vary significantly in performance: from around 10kHz (for an unoptimized
interpreter modelling full address translation on every instruction fetch) to
500MHz for metatracing simulators like Pydgin [[lockhart:ispass:2015]].



### Testing architecture design

ISA specifications are as prone to bugs as any other software of similar size
and complexity.  Fonseca et al.'s empirical study of the correctness of
formally verified systems found bugs in specifications [[fonseca:esc:2017]].
So, before an ISA specification can be considered trustworthy, it must be
tested or verified against
an accurate oracle [[barr:tse:2015]] (usually hardware).

Different specification development efforts vary significantly in how much
testing they perform: from a few 10s of tests per instruction to executing billions of instructions and booting OSes
[[fox:itp:2010],
[goel:fmcad:2014],
[flur:popl:2016],
[shi:phd:2013],
[reid:fmcad:2016],
[armstrong:popl:2019]].

Formal verification of a processor against
a specification
[[hunt:jar:1989],
[fox:ucam:2002],
[reid:cav:2016]]
has the desirable
side-effect of detecting bugs in the specification and ensuring compatibility.


### Automatic generation of test cases

Building a good testsuite is very laborious and error-prone but some of
the effort can be avoided by automatically generating test cases.
[[martignoni:asplos:2012],
[godefroid:acmq:2012],
[campbell:fmics:2014]].

In my experience though, most commonly used test generation techniques focus on
achieving consistent levels of control-coverage (i.e., they focus on control
flow graphs) and they are relatively weak at achieving consistent value
coverage.  In my adaptation of the concolic testcase generation technique
described in [[martignoni:asplos:2012]], I was happy with the tests generated
for instructions that set condition flags (e.g., ADD).  Unfortunately, for
instructions with just one control path such as signed multiply (SMUL), just
one test would be generated when even the weakest hand-written testsuite would
test for all combinations of positive, zero, and negative operands and would
test for various overflow conditions.  I feel that we still have more to learn
here.


### Verifying architecture design

We can use testing and verification to check that a specification matches
existing implementations of an ISA.  But we hit a chicken-and-egg situation
when we want to check extensions to the specification: testsuites and
processors are created *after* the specification is written so they cannot be
used to test the specification as it is being written.

The solution used in [[reid:oopsla:2017]] and [[bauereiss:ucam:2021]] is to
identify and formally verify important properties that the architecture must
satisfy if it is to achieve its purpose and is not to break existing properties
of the architecture. Often, the most important things to verify are security properties.


## Verifying processor pipelines

With processor complexity rising (an inevitable result of both commercial pressures and the end of Moore's law), formal verification of processors is increasingly important.
Some processors that have been formally verified against their ISA specification include
FM8502  [[hunt:jar:1989]],
ARM6  [[fox:ucam:2002]],
DLX  [[beyer:ijsttt:2006]],
five Arm processors [[reid:cav:2016]],
Y86-64 [[bryant:cmu:2018]],
Silver [[loow:pldi:2019]],
and
x86 [[goel:spisa:2019], [goel:cpp:2020], [goel:cav:2021]].


## Compilers

### Compiler generators

Barbacci developed Bell and Newell's ISP notation into a machine readable
notation "Instruction Set Processor Semantics"  (ISPS)
[[barbacci2:computer:1973], [barbacci:ieee:1981]] that targets compiler-related
uses such as the automatic derivation of compiler code
generators by
Fraser [[fraser:sigart:1977]]
that used ISP specifications of the IBM-360 and PDP-10
and Cattell [[cattell:toplas:1980]]
that used ISPS specifications
of the IBM-360, PDP-8, PDP-10, PDP-11, Intel 8080, and Motorola 6800.

This topic seems to have largely died off until instruction selection in SLED
[[dias:popl:2010]].

### Discovery, verification and synthesis of peephole optimisations

One part of compilation that is especially well suited to
automation is the discovery / generation of peephole optimizations
using "superoptimization" [[massalin:asplos:1987]] (an exhaustive search).
For example, 
Bansal's superoptimizer [[bansal:asplos:2006]],
Denali [[joshi:pldi:2002]], and
Souper [[mukherjee:oopsla:2020]].
Where peephole optimizations are discovered and implemented manually,
tools like Alive [[lopes:pldi:2015]] can be used to verify
that the optimizations are correct.


### Verifying compilers

Some of the earliest uses of formal semantics were for automatic reasoning
about programs such as Samet's development of Translation
Validation [[samet:ieeetse:1977], [samet:phd:1975]]
(later reinvented and refined by Pnuelli [[pnueli:tacas:1998]]
and Necula [[necula:popl:1997]]).

Verifying a simple "compiler" is now often part of masters / doctoral - level courses
on using interactive theorem provers,
some more complete compiler verifications include

- CompCert C compiler [[leroy:cacm:2009]],
- LISP compiler [[myreen:tphols:2009]],
- JIT compiler for LISP [[myreen:popl:2010]],
- Milawi theorem prover [[myreen:itp:2011]],
- CakeML compiler
  [[kumar:popl:2014],
  [fox:cpp:2017],
  [tan:icfp:2016]], and
- LLVM C compiler [[lopes:pldi:2021]].


## Software security

Both "white-hat" and "black-hat" security engineers analyze binaries
to find vulnerabilities and to construct signatures for detecting malware.

Some of the [binary analysis] tools used are 

- The [Mayhem][mayhem] [automatic exploit generation] tool [[cha:sandp:2012]]
  based on CMU's [BAP binary analysis platform][BAP tool] [[brumley:cav:2011]].

- The [angr][angr tool] tool [[coppa:ase:2017]] that uses [valgrind] to
  convert binary code to the VEX intermediate representation that is then
  symbolically executed.

- The [McSema][mcsema tool] [binary lifter] that uses the [Remill library] and IDA Pro to convert
  ("lift") binary machine code into [LLVM][LLVM compiler] code.

- The Binsec/Rel relational symbolic execution that checks that binary
  code is constant time [[daniel:sandp:2020]].

- [[mycroft:esop:1999]] and [[noonan:pldi:2016]] describe how to decompile machine
  code to higher-level languages.

- The [Serval][serval] [symbolic evaluation] tool is used to verify machine code microkernels,
  LLVM code and Linux BPF code [[nelson:sosp:2019]].

- [[dasgupta:pldi:2020]] and [[hendrix:itp:2019]] describe the generation
  and checking of binary lifters.

- [[regehr:emsoft:2003],
  [regehr:asplos:2004],
  [regehr:lctes:2006]]
  describe the automatic generation and use of abstract transfer
  functions to analyze binary programs.

- [[shoshitaishvili:sp:2016]] is a recent(ish) survey of offensive techniques.

With the exception of [[dasgupta:pldi:2020]], none of these currently use
formal ISA specifications.  However, as the arms race between attackers and
defenders hots up, there is an increasing need for the completeness and
trustworthiness of a full formal ISA spec.


## Verifying software

Last but not least is the use of ISA specifications is to verify software.


- Windows hypervisor code [[maus:amast:2008]].
- Hoare logic for machine code[[myreen:fse:2007]].
- Separation logic for machine code [[jensen:popl:2013]].
- Generating abstract interpreters for machine code [[lim:toplas:2013]].
- Parts of a operating system [[goel:fmcad:2014], [goel:phd:2016]].
- The SeL4 capability-based microkernel[[klein:sosp:2009], [sewell:pldi:2013]].
- A tiny Arm hypervisor [[dam:trusted:2013], [baumann:eucnc:2016]].
- The Vale tool for writing verified assembly language [[bond:usenix:2017]].
- Verification in the presence of TLBs[[syeda:itp:2018]] (see also [[simner:pls:2020]]).
- A symbolically executable hypervisor [[nordholz:eurosys:2020]].
- The Isla symbolic execution tool based on SAIL [[armstrong:cav:2021]].
- The SeKVM hypervisor [[li:usenix:2021]].
- An Arm hypervisor[[tao:sosp:2021]].
- Proving LTL properties of binaries [[liu:arxiv:2021]].
- Generating instruction encoders/decoders [[xu:cav:2021]].

-----------

[aagaard:charme:2001]:         {{site.RWurl}}/papers/aagaard:charme:2001/
[aagaard:fmcad:2000]:          {{site.RWurl}}/papers/aagaard:fmcad:2000/
[alglave:toplas:2014]:         {{site.RWurl}}/papers/alglave:toplas:2014/
[amadio:fpara:2014]:           {{site.RWurl}}/papers/amadio:fpara:2014/
[armstrong:arw:2018]:          {{site.RWurl}}/papers/armstrong:arw:2018/
[armstrong:cav:2021]:          {{site.RWurl}}/papers/armstrong:cav:2021/
[armstrong:popl:2019]:         {{site.RWurl}}/papers/armstrong:popl19:2019/
[armstrong:spisa:2019]:        {{site.RWurl}}/papers/armstrong:spisa:2019/
[avgerinos:icse:2014]:         {{site.RWurl}}/papers/avgerinos:icse:2014/
[bansal:asplos:2006]:          {{site.RWurl}}/papers/bansal:asplos:2006/
[bansal:osdi:2008]:            {{site.RWurl}}/papers/bansal:osdi:2008/
[barbacci:cmu:1972]:           {{site.RWurl}}/papers/barbacci:cmu:1972/
[barbacci:ieee:1981]:          {{site.RWurl}}/papers/barbacci:ieee:1981/
[barbacci2:computer:1973]:     {{site.RWurl}}/papers/barbacci2:computer:1973/
[barr:tse:2015]:               {{site.RWurl}}/papers/barr:tse:2015/
[bauereiss:ucam:2021]:         {{site.RWurl}}/papers/bauereiss:ucam:2021/
[baumann:eucnc:2016]:          {{site.RWurl}}/papers/baumann:eucnc:2016/
[bell:afips:1970]:             {{site.RWurl}}/papers/bell:afips:1970/
[bell:book:1971]:              {{site.RWurl}}/papers/bell:book:1971/
[bevier:jar:1989]:             {{site.RWurl}}/papers/bevier:jar:1989/
[beyer:ijsttt:2006]:           {{site.RWurl}}/papers/beyer:ijsttt:2006/
[bishop:jacm:2019]:            {{site.RWurl}}/papers/bishop:jacm:2019/
[blanqui:rapido:2011]:         {{site.RWurl}}/papers/blanqui:rapido:2011/
[bond:usenix:2017]:            {{site.RWurl}}/papers/bond:usenix:2017/
[boulton:tpcd:1993]:           {{site.RWurl}}/papers/boulton:tpcd:1993/
[brumley:cav:2011]:            {{site.RWurl}}/papers/brumley:cav:2011/
[bryant:cmu:2018]:             {{site.RWurl}}/papers/bryant:cmu:2018/
[burch:cav:1994]:              {{site.RWurl}}/papers/burch:cav:1994/
[campbell:fmcad:2016]:         {{site.RWurl}}/papers/campbell:fmcad:2016/
[campbell:fmics:2014]:         {{site.RWurl}}/papers/campbell:fmics:2014/
[cattell:phd:1978]:            {{site.RWurl}}/papers/cattell:phd:1978/
[cattell:toplas:1980]:         {{site.RWurl}}/papers/cattell:toplas:1980/
[cha:sandp:2012]:              {{site.RWurl}}/papers/cha:sandp:2012/
[cifuentes:computer:2000]:     {{site.RWurl}}/papers/cifuentes:computer:2000/
[cifuentes:iwpc:1998]:         {{site.RWurl}}/papers/cifuentes:iwpc:1998/
[cock:ccs:2014]:               {{site.RWurl}}/papers/cock:ccs:2014/
[coppa:ase:2017]:              {{site.RWurl}}/papers/coppa:ase:2017/
[dam:ted:2013]:                {{site.RWurl}}/papers/dam:ted:2013/
[dam:trusted:2013]:            {{site.RWurl}}/papers/dam:trusted:2013/
[daniel:sandp:2020]:           {{site.RWurl}}/papers/daniel:sandp:2020/
[dasgupta:pldi:2019]:          {{site.RWurl}}/papers/dasgupta:pldi:2019/
[dasgupta:pldi:2020]:          {{site.RWurl}}/papers/dasgupta:pldi:2020/
[degenbaev:phd:2012]:          {{site.RWurl}}/papers/degenbaev:phd:2012/
[dias:popl:2010]:              {{site.RWurl}}/papers/dias:popl:2010/
[falkoff:ibm:1964]:            {{site.RWurl}}/papers/falkoff:ibm:1964/
[fauth:edtc:1995]:             {{site.RWurl}}/papers/fauth:edtc:1995/
[fernandez:icse:1997]:         {{site.RWurl}}/papers/fernandez:icse:1997/
[flur:popl:2016]:              {{site.RWurl}}/papers/flur:popl:2016/
[flur:popl:2017]:              {{site.RWurl}}/papers/flur:popl:2017/
[fonseca:esc:2017]:            {{site.RWurl}}/papers/fonseca:esc:2017/
[fox:cambridge:2001]:          {{site.RWurl}}/papers/fox:cambridge:2001/
[fox:cpp:2017]:                {{site.RWurl}}/papers/fox:cpp:2017/
[fox:itp:2010]:                {{site.RWurl}}/papers/fox:itp:2010/
[fox:itp:2012]:                {{site.RWurl}}/papers/fox:itp:2012/
[fox:itps:2015]:               {{site.RWurl}}/papers/fox:itps:2015/
[fox:tphols:2003]:             {{site.RWurl}}/papers/fox:tphols:2003/
[fox:ucam:2002]:               {{site.RWurl}}/papers/fox:ucam:2002/
[fraser:sigart:1977]:          {{site.RWurl}}/papers/fraser:sigart:1977/
[ge:jce:2016]:                 {{site.RWurl}}/papers/ge:jce:2016/
[godefroid:acmq:2012]:         {{site.RWurl}}/papers/godefroid:acmq:2012/
[godefroid:pldi:2012]:         {{site.RWurl}}/papers/godefroid:pldi:2012/
[goel:acl2:2013]:              {{site.RWurl}}/papers/goel:acl2:2013/
[goel:cav:2021]:               {{site.RWurl}}/papers/goel:cav:2021/
[goel:cpp:2020]:               {{site.RWurl}}/papers/goel:cpp:2020/
[goel:fmcad:2014]:             {{site.RWurl}}/papers/goel:fmcad:2014/
[goel:pcs:2017]:               {{site.RWurl}}/papers/goel:pcs:2017/
[goel:phd:2016]:               {{site.RWurl}}/papers/goel:phd:2016/
[goel:spisa:2019]:             {{site.RWurl}}/papers/goel:spisa:2019/
[gray:micro:2015]:             {{site.RWurl}}/papers/gray:micro:2015/
[greve:fmcad:1998]:            {{site.RWurl}}/papers/greve:fmcad:1998/
[hardin:acl2:2006]:            {{site.RWurl}}/papers/hardin:acl2:2006/
[hendrix:itp:2019]:            {{site.RWurl}}/papers/hendrix:itp:2019/
[hennessy:micro:1982]:         {{site.RWurl}}/papers/hennessy:micro:1982/
[heule:pldi:2016]:             {{site.RWurl}}/papers/heule:pldi:2016/
[higgins:hldvt:2004]:          {{site.RWurl}}/papers/higgins:hldvt:2004/
[hsiao:micro:2021]:            {{site.RWurl}}/papers/hsiao:micro:2021/
[huang:todaes:2019]:           {{site.RWurl}}/papers/huang:todaes:2019/
[hunt:jar:1989]:               {{site.RWurl}}/papers/hunt:jar:1989/
[jensen:popl:2013]:            {{site.RWurl}}/papers/jensen:popl:2013/
[jhala:cav:2001]:              {{site.RWurl}}/papers/jhala:cav:2001/
[jiang:arxiv:2021]:            {{site.RWurl}}/papers/jiang:arxiv:2021/
[joloboff:dsetta:2015]:        {{site.RWurl}}/papers/joloboff:dsetta:2015/
[joshi:pldi:2002]:             {{site.RWurl}}/papers/joshi:pldi:2002/
[kaivola:cav:2009]:            {{site.RWurl}}/papers/kaivola:cav:2009/
[kaufmann:acl2:1997]:          {{site.RWurl}}/papers/kaufmann:acl2:1997/
[kaufmann:utaustin:2012]:      {{site.RWurl}}/papers/kaufmann:utaustin:2012/
[kennedy:ppdp:2013]:           {{site.RWurl}}/papers/kennedy:ppdp:2013/
[kirankumar:fmcad:2012]:       {{site.RWurl}}/papers/kirankumar:fmcad:2012/
[klein:sosp:2009]:             {{site.RWurl}}/papers/klein:sosp:2009/
[kocher:arxiv:2018]:           {{site.RWurl}}/papers/kocher:arxiv:2018/
[kroening:itg:2000]:           {{site.RWurl}}/papers/kroening:itg:2000/
[kuhne:fmcad:2010]:            {{site.RWurl}}/papers/kuhne:fmcad:2010/
[kumar:popl:2014]:             {{site.RWurl}}/papers/kumar:popl:2014/
[lahiri:cav:2003]:             {{site.RWurl}}/papers/lahiri:cav:2003/
[lahiri:hldvt:2001]:           {{site.RWurl}}/papers/lahiri:hldvt:2001/
[leroy:cacm:2009]:             {{site.RWurl}}/papers/leroy:cacm:2009
[li:usenix:2021]:              {{site.RWurl}}/papers/li:usenix:2021/
[lim:toplas:2013]:             {{site.RWurl}}/papers/lim:toplas:2013/
[lipp:arxiv:2018]:             {{site.RWurl}}/papers/lipp:arxiv:2018/
[liu:arxiv:2021]:              {{site.RWurl}}/papers/liu:arxiv:2021/
[lockhart:ispass:2015]:        {{site.RWurl}}/papers/lockhart:ispass:2015/
[loow:pldi:2019]:              {{site.RWurl}}/papers/loow:pldi:2019/
[lopes:pldi:2015]:             {{site.RWurl}}/papers/lopes:pldi:2015/
[lopes:pldi:2021]:             {{site.RWurl}}/papers/lopes:pldi:2021/
[martignoni:asplos:2012]:      {{site.RWurl}}/papers/martignoni:asplos:2012/
[massalin:asplos:1987]:        {{site.RWurl}}/papers/massalin:asplos:1987/
[maus:amast:2008]:             {{site.RWurl}}/papers/maus:amast:2008/
[mcilroy:arxiv:2019]:          {{site.RWurl}}/papers/mcilroy:arxiv:2019/
[mcmillan:cav:1998]:           {{site.RWurl}}/papers/mcmillan:cav:1998/
[mishra:book:2008]:            {{site.RWurl}}/papers/mishra:book:2008/
[morrisett:pldi:2012]:         {{site.RWurl}}/papers/morrisett:pldi:2012/
[mukherjee:oopsla:2020]:       {{site.RWurl}}/papers/mukherjee:oopsla:2020/
[mulligan:icfp:2014]:          {{site.RWurl}}/papers/mulligan:icfp:2014/
[mycroft:esop:1999]:           {{site.RWurl}}/papers/mycroft:esop:1999/
[myreen:fse:2007]:             {{site.RWurl}}/papers/myreen:fse:2007/
[myreen:itp:2011]:             {{site.RWurl}}/papers/myreen:itp:2011/
[myreen:itp:2012]:             {{site.RWurl}}/papers/myreen:itp:2012/
[myreen:popl:2010]:            {{site.RWurl}}/papers/myreen:popl:2010/
[myreen:tphols:2009]:          {{site.RWurl}}/papers/myreen:tphols:2009/
[necula:popl:1997]:            {{site.RWurl}}/papers/necula:popl:1997/
[nelson:sosp:2019]:            {{site.RWurl}}/papers/nelson:sosp:2019/
[nethercote:pldi:2007]:        {{site.RWurl}}/papers/nethercote:pldi:2007/
[noonan:pldi:2016]:            {{site.RWurl}}/papers/noonan:pldi:2016/
[nordholz:eurosys:2020]:       {{site.RWurl}}/papers/nordholz:eurosys:2020/
[pdp11:book:1973]:             {{site.RWurl}}/papers/pdp11:book:1973/
[pnueli:tacas:1998]:           {{site.RWurl}}/papers/pnueli:tacas:1998/
[pulte:popl:2017]:             {{site.RWurl}}/papers/pulte:popl:2017/
[ramsey:lctes:1998]:           {{site.RWurl}}/papers/ramsey:lctes:1998/
[ramsey:toplas:1997]:          {{site.RWurl}}/papers/ramsey:toplas:1997/
[regehr:asplos:2004]:          {{site.RWurl}}/papers/regehr:asplos:2004/
[regehr:emsoft:2003]:          {{site.RWurl}}/papers/regehr:emsoft:2003/
[regehr:lctes:2006]:           {{site.RWurl}}/papers/regehr:lctes:2006/
[regehr:tecs:2005]:            {{site.RWurl}}/papers/regehr:tecs:2005/
[reid:cav:2016]:               {{site.RWurl}}/papers/reid:cav:2016/
[reid:fmcad:2016]:             {{site.RWurl}}/papers/reid:fmcad:2016/
[reid:msc:1994]:               {{site.RWurl}}/papers/reid:msc:1994/
[reid:oopsla:2017]:            {{site.RWurl}}/papers/reid:oopsla:2017/
[reid:phd:2019]:               {{site.RWurl}}/papers/reid:phd:2019/
[roessle:cpp:2019]:            {{site.RWurl}}/papers/roessle:cpp:2019/
[rondon:pldi:2008]:            {{site.RWurl}}/papers/rondon:pldi:2008/
[samet:ieeetse:1977]:          {{site.RWurl}}/papers/samet:ieeetse:1977/
[samet:phd:1975]:              {{site.RWurl}}/papers/samet:phd:1975/
[sarkar:pldi:2011]:            {{site.RWurl}}/papers/sarkar:pldi:2011/
[sarkar:popl:2009]:            {{site.RWurl}}/papers/sarkar:popl:2009/
[schmaltz:vstte:2012]:         {{site.RWurl}}/papers/schmaltz:vstte:2012/
[seal:book:2000]:              {{site.RWurl}}/papers/seal:book:2000/
[sevcik:jacm:2013]:            {{site.RWurl}}/papers/sevcik:jacm:2013/
[sewell:cacm:2010]:            {{site.RWurl}}/papers/sewell:cacm:2010/
[sewell:pldi:2013]:            {{site.RWurl}}/papers/sewell:pldi:2013/
[shi:phd:2013]:                {{site.RWurl}}/papers/shi:phd:2013/
[shoshitaishvili:sp:2016]:     {{site.RWurl}}/papers/shoshitaishvili:sp:2016/
[simner:pls:2020]:             {{site.RWurl}}/papers/simner:pls:2020/
[slobodova:memocode:2011]:     {{site.RWurl}}/papers/slobodova:memocode:2011/
[srinivasan:ieeetoc:2010]:     {{site.RWurl}}/papers/srinivasan:ieeetoc:2010/
[stephens:micro:2017]:         {{site.RWurl}}/papers/stephens:micro:2017/
[su:computer:1974]:            {{site.RWurl}}/papers/su:computer:1974/
[syeda:itp:2018]:              {{site.RWurl}}/papers/syeda:itp:2018/
[tan:icfp:2016]:               {{site.RWurl}}/papers/tan:icfp:2016/
[tao:sosp:2021]:               {{site.RWurl}}/papers/tao:sosp:2021/
[watson:sandp:2015]:           {{site.RWurl}}/papers/watson:sandp:2015/
[windley:ieeetoc:1995]:        {{site.RWurl}}/papers/windley:ieeetoc:1995/
[woodruff:isca:2014]:          {{site.RWurl}}/papers/woodruff:isca:2014/
[xi:jfp:2007]:                 {{site.RWurl}}/papers/xi:jfp:2007/
[xu:cav:2021]:                 {{site.RWurl}}/papers/xu:cav:2021/
[zhang:fmcad:2018]:            {{site.RWurl}}/papers/zhang:fmcad:2018/
[zivojnovic:vlsi:1996]:        {{site.RWurl}}/papers/zivojnovic:vlsi:1996/
[zorn:iscawddd:2017]:          {{site.RWurl}}/papers/zorn:iscawddd:2017/

[BAP tool]:                    {{site.RWurl}}/notes/bap-tool/
[LLVM compiler]:               {{site.RWurl}}/notes/LLVM-compiler/
[acl2-theorem-prover]:         {{site.RWurl}}/notes/acl2-theorem-prover/
[angr tool]:                   {{site.RWurl}}/notes/angr-verifier/
[automatic exploit generation]:{{site.RWurl}}/notes/automatic-exploit-generation/
[binary analysis]:             {{site.RWurl}}/notes/binary-analysis/
[binary lifter]:               {{site.RWurl}}/notes/binary-lifter/
[coq-theorem-prover]:          {{site.RWurl}}/notes/coq-theorem-prover/
[cvc4-solver]:                 {{site.RWurl}}/notes/cvc4-solver/
[hol-theorem-prover]:          {{site.RWurl}}/notes/hol-theorem-prover/
[isabelle-theorem-prover]:     {{site.RWurl}}/notes/isabelle-theorem-prover/
[mayhem]:                      {{site.RWurl}}/notes/mayhem/
[mcsema tool]:                 {{site.RWurl}}/notes/mcsema-tool/
[remill library]:              {{site.RWurl}}/notes/remill-library/
[serval]:                      {{site.RWurl}}/notes/serval-tool/
[symbolic evaluation]:         {{site.RWurl}}/notes/symbolic-evaluation/
[valgrind]:                    {{site.RWurl}}/notes/valgrind/
[z3-solver]:                   {{site.RWurl}}/notes/z3-solver/


[jaspergold]:                  https://www.cadence.com/ko_KR/home/tools/system-design-and-verification/formal-and-static-verification/jasper-gold-verification-platform.html
[symbiyosys]:                  https://symbiyosys.readthedocs.io/
