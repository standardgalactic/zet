---
title: Using ASLi with Arm's v8.6-A ISA specification
layout: post
---

![ARM logo]({{ site.baseurl }}/images/ARM_logo.svg){: style="float: left; width: 10%; padding: 1%"}
[ASLi](https://github.com/alastairreid/asl-interpreter)
is an interpreter for
[Arm's Architecture Specification Language]({{ site.baseurl }}{% post_url 2016-08-17-specification_languages %}).
To use it, you need to download the 
[MRA tools](https://github.com/alastairreid/mra_tools),
Arm's
[Architecture Specifications](https://developer.arm.com/architectures/cpu-architecture/a-profile/exploration-tools)
and, of course,
[ASLi](https://github.com/alastairreid/asl-interpreter).
(Note: that I am linking to an updated version of ASLi
instead of to
[Arm's official release](https://github.com/ARM-software/asl-interpreter)
– I had to extend ASLi a bit to be able to execute programs with it.)

## Installing tools

First, setup OCaml with all the libraries you will need.
(These instructions are for MacOS.)
```
brew install opam gmp mpir
opam install ocaml.4.09.0 menhir ocamlfind ott linenoise pprint z3.4.7.1
env CFLAGS="-I$HOME/homebrew/include/" LDFLAGS="-L$HOME/homebrew/lib/" opam install zarith
eval `opam config env`
export DYLD_LIBRARY_PATH=`opam config var z3:lib`
```

On Linux, the following is probably what you need (untested)
```
sudo apt-get install opam gmp mpir
opam install ocaml.4.09.0 menhir ocamlfind ott linenoise pprint z3.4.7.1 zarith
eval `opam config env`
export LD_LIBRARY_PATH=`opam config var z3:lib`
```

These commands may take a while to run ...

Once you have installed OCaml, download and build the tools as follows
```
git clone https://github.com/alastairreid/mra_tools.git
git clone https://github.com/alastairreid/asl-interpreter.git
make -C asl-interpreter asli
```

## Downloading Arm's specification

Once you have the tools setup, download the Arm specification
```
pushd mra_tools
mkdir -p v8.6
pushd v8.6

wget https://developer.arm.com/-/media/developer/products/architecture/armv8-a-architecture/2019-12/SysReg_xml_v86A-2019-12.tar.gz
wget https://developer.arm.com/-/media/developer/products/architecture/armv8-a-architecture/2019-12/A64_ISA_xml_v86A-2019-12.tar.gz
wget https://developer.arm.com/-/media/developer/products/architecture/armv8-a-architecture/2019-12/AArch32_ISA_xml_v86A-2019-12.tar.gz

tar zxf A64_ISA_xml_v86A-2019-12.tar.gz
tar zxf AArch32_ISA_xml_v86A-2019-12.tar.gz
tar zxf SysReg_xml_v86A-2019-12.tar

popd
```
and unpack the specification using the mra_tools scripts
```
make all
popd
```
This extracts the ASL code from the XML files that Arm distributes it in,
generates declarations of all the system registers and
patches some minor type errors in the ASL code.
(The patches are required because ASLi has slightly stricter typechecking
than the default configuration of Arm's internal tool.)

The mra_tools repository also contains some support code that turns Arm's
specification into a simulator.  This is in the directory mra_tools/support.
```
$ ls mra_tools/support
README.txt      debug.asl       hints.asl       stubs.asl
aes.asl         feature.asl     interrupts.asl  usermode.asl
barriers.asl    fetchdecode.asl memory.asl
```

## Running ASLi

You can run ASLi directly
```
cd asl-interpreter
./asli
```
This loads the ASL standard library and then prints the following banner that
may feel familiar to users of Haskell interpreters like Hugs or GHCi.
```
            _____  _       _    ___________________________________
    /\     / ____|| |     (_)   ASL interpreter
   /  \   | (___  | |      _    Copyright Arm Limited (c) 2017-2019
  / /\ \   \___ \ | |     | |
 / ____ \  ____) || |____ | |   ASL 0.1 alpha
/_/    \_\|_____/ |______||_|   ___________________________________

Type :? for help
```
ASLi is an interactive environment and you can type ASL expressions and ASL
statements and see the result.
(ASL statements must end with a semicolon for ASLi to execute them.)
```
ASLi> 1+1
2
ASLi> ZeroExtend('11', 32)
'00000000000000000000000000000011'
ASLi> bits(32) x = ZeroExtend('11', 32);
ASLi> x
'00000000000000000000000000000011'
```
You can also type commands starting with colon such as ":help".

You can also tell ASLi to generate a trace as it executes using commands like
this that trace calls to functions
```
:set +trace:fun
```
For example, you can see evaluating ZeroExtend calls the function Zeros.
```
ASLi> :set +trace:fun
ASLi> ZeroExtend('11', 32)
TRACE funcall: ZeroExtend.0  [2] [32] 2'11' 32
TRACE funcall: Zeros.0  [30] 30
32'00000000000000000000000000000011'
```

## Running Arm's specification

Once the specification is unpacked, we can use ASLi to parse and typecheck all
the files
```
./asli prelude.asl ../mra_tools/arch/regs.asl ../mra_tools/types.asl ../mra_tools/arch/arch.asl ../mra_tools/arch/arch_instrs.asl ../mra_tools/arch/arch_decode.asl ../mra_tools/support/aes.asl ../mra_tools/support/barriers.asl ../mra_tools/support/debug.asl ../mra_tools/support/feature.asl ../mra_tools/support/hints.asl ../mra_tools/support/interrupts.asl ../mra_tools/support/memory.asl ../mra_tools/support/stubs.asl ../mra_tools/support/fetchdecode.asl
```
Arm's architecture specification can be configured to match the behaviour of
particular processors by specifying certain "implementation defined"
constants.
This is done using commands like the following.
```
:set impdef "Maximum Physical Address Size" = 52
:set impdef "Maximum Virtual Address Size"  = 56
:set impdef "Reserved Intermediate Physical Address size value" = 52
```
Before running a program, you need to reset the processor
```
__TakeColdReset();
```
load a binary file and set the program counter and the stack pointer
to appropriate addresses
```
:elf tests/test_O2.elf
_PC  = 0x400168[63:0];
SP[] = 0x100000[63:0];
```
and run the program
```
:run
```
The example binary writes the word "Test" to a serial port
and then writes the ASCII character EOT (end of transmission)
to stop the interpreter.
This produces output like this
```
Loading ELF file tests/test_O2.elf.
Entry point = 0x400168
Test
Program exited by writing ^D to TUBE
Exception taken
```

All these commands are in the "project" file "tests/test.prj" and
can be executed using the ":project" command
```
:project tests/test.prj
```

## Limitations

There are a few limitations on what I have done so far

* I did virtually no testing.  If you try any other binaries, you might
  use some ASL feature that has not been tested yet and find a bug.
* The ELF loader only works for 64-bit little-endian files.
  So if you want to try 32-bit binaries or mixed endian tests, you will have
  to extend the ELF loader.  (This is surprisingly easy to do.)
* Most seriously, the mra_tools scripts cannot generate all the ASL
  required to fully implement system registers.
  So it is very, very unlikely that you can boot Linux with what
  is there at the moment.
  It would be great if Arm would publicly release the system register support code
  they have internally.

## Conclusions

OK, that's enough for one post...

Enjoy!
