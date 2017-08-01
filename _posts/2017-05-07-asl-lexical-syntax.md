---
layout: post
title: ASL Lexical Syntax
---

In my post about [dissecting the ARM Machine Readable Architecture files]({{ site.baseurl }}{% post_url 2017-04-29-dissecting-ARM-MRA %})
I described how to extract the ASL code from the XML files that ARM provides.
In this post, I will describe how to start processing that code by examining
the lexical syntax.
In doing so, I will be going back to one of the first things I had to figure
out when I started trying to use ARM's documentation as an executable
specification so I will be looking at code I have barely thought about in
6 years and trying to remember my thought processes at the time as
I reverse engineered the language lurking inside ARM's pseudocode.

There are two aspects to ASL's lexical syntax: tokens and indentation.

## Tokens

For the most part, ASL is a conventional C-like token syntax.
Files are plain ASCII and tokens are defined as follows.

- Identifiers start with a letter or underscore and continue with zero or more
  letters, underscores or digits.

  It is almost true that only global variables, constants, functions and user-defined types
  begin with an uppercase letter and only local variables and formal parameters
  of functions begin with a lowercase letter, but it is not 100% true.
  It is also almost true that names don't begin with an underscore but there
  are also a few exceptions.

  My implementation also allows dollar-signs in identifiers and it
  also borrows a trick from Scala and allows any sequence of characters
  enclosed in backticks to be used as an identifier; this is useful if you want
  to define builtin functions such as `+` and `/`.
  Neither of these extensions appear in the published specification.

- Qualified identifiers are identifiers that additionally contain a single
  decimal point character.  For example "AArch32.CallSupervisor".

  My implementation currently detects these in the parser and treats them
  as distinct from identifiers because the original plan for how we would use
  qualified identifiers changed after we started using them.  I might go back
  and clean this up sometime.

- Integers are written either in decimal using one or more of the
  characters 0-9 or in hexadecimal using '0x' at the start followed by the
  characters 0-9, a-f, A-F and underscore.
  Fixed point numbers are written in decimal and consist of one or more decimal
  digits, a decimal point and one or more decimal digits.

  The underscores in hexadecimal numbers are not significant and their only
  purpose is to make large constants such as 0xefff_fffe or 0x8000_0000_0000_0000 easier to read.

- Constant bit-vectors (called bit-strings in ARM's documentation) are written using 1, 0 and spaces
  surrounded by single-quotes.  The spaces are not significant and are only
  used to improve readability of long constants so '1111 1111 1111 1111' is the
  same as '1111111111111111'.

- Constant bit-masks are written using 1, 0, x and spaces
  surrounded by single-quotes.  The x represents a don't care character
  and spaces are only used to improve readability.

- Strings are surrounded by double-quotes.

  Strings play only a minor role in
  the architecture specifications so there are no escape mechanisms
  to allow strings to contain control characters or double quotes.

  In the v7-A specifications, masks were written using both single and
  double-quotes.  In v8-A, masks are only written using single-quotes.

- The following character sequences are used as delimiters:
  "(", ")", "[", "]", "{", "}", "+", "-", "\*", "/", "!", "^", "&&", "||",
  "==", "!=", "<=", ">=", "<", ">", "\<<", "\>>", "=", ";", ",", ".", ":", "\..",
  "+:", "&", "++".

  Of these, the most unfamiliar is probably "+:" which is used to define a
  bitslice of a particular width.  For example "v<4 +: 8>" represents the 8-bit long
  bit vector consisting of bits 4, 5, ... 11 of variable v.
  Unlike C, the operator "^" represents exponentiation, not xor.

  A symbol representing implication is in the process of being added - we have not
  settled on "\-->", "->", "==>" or "=>".


- The following identifiers are reserved words:
  "if", "then", "elsif", "else", "case", "of", "when", "otherwise", "for", "to", "downto",
  "while", "do", "repeat", "until", "return", "assert", "Consistent",
  "enumeration", "constant", "is", "array", "bit",
  "QUOT", "REM", "DIV", "MOD", "AND", "NOT", "OR", "EOR", "IN",
  "UNDEFINED", "UNKNOWN", "UNPREDICTABLE", "CONSTRAINED_UNPREDICTABLE", "SEE",
  "IMPLEMENTATION_DEFINED", "SUBARCHITECTURE_DEFINED",
  "RAISE", "try", "catch", "throw",
  "is", "typeof", "TypeOf".

  "typeof" and "TypeOf" are synonyms --- we have not committed
  to whether to use lowercase or CamelCase but "typeof" is by far the most common.

  "in" is currently implemented as a reserved word as well and is a synonym for "IN"
  but I believe that we have eliminated all uses of "in" and it could be retired.

  The following identifiers are also implemented but are not found in the published
  parts of ARM's specifications.
  "__type", "__register", "__forall", "__newevent", "__event", "__newmap", "__map",
  "__config", "__intersect", "__namespace", "__overloaded".
  I will say more about these when describing the ASL grammar.

- Comments can be written in two styles.  The dominant style begins with "//" and
  lasts until the end of the line but the classic C-style surrounded by "/\*" and "\*/"
  is also supported.  The latter style can be nested.

In addition to the above, we recognise the "#-line" markers inserted by the C preprocessor
to indicate that a file was "#include"d or that a section of code was omitted due to use of "#ifdef".


## Indentation

ASL follows the example of Occam, Haskell and Python of using indentation to indicate
structure instead of requiring some form of "parentheses" such as "{"/"}", "begin"/"end", etc.

The way this is implemented is that the we have three additional tokens "NEWLINE", "INDENT" (indicating
an increase in indentation since the last non-empty, non-comment line) and "DEDENT" (indicating
a decrease in indentation since the last non-empty, non-comment line).

As we are processing a file, we maintain a stack of indentation depths.
On the first token of each line, we compare the indentation of that token with the depth on top of the stack.

- If the indentation is greater, we emit a single "INDENT" token and push the new indentation onto the stack.
- If the indentation is less and the stack contains that indentation depth, we pop the stack back to that depth
  and emit a corresponding number of "DEDENT" tokens.
- It is an error if the current indentation is not present in the stack.

These indentation rules are inconvenient in multi-line expressions and ASL follows Python
by treating multiple lines as a single line inside certain pairs of tokens:

- "(" and ")"; "[" and "]"; "{" and "}"
- "if" or "elsif" and "then"
- "while" and "do"


There is a special circle of hell reserved for those who use tabs in source
files.  Offenders are doomed to endless arguments with those whose editors use
a different tab alignment.  That said, the current implementation of ASL follows
Haskell and defines tab alignment as 8 but it should really be reported as an
error.
All ARM specifications use a 4-character indentation increment but that is not required by ASL.

## Combining the two

The implementation implements these two parts by having two nested lexers.
The inner lexer is a conventional lexer for identifiers, numbers, symbols, reserved
words, etc. and tags all tokens with a line number and column number.
The outer lexer implements the indentation rules and uses the location
information to insert additional NEWLINE, INDENT and DEDENT tokens.

### Related posts and papers

* Paper: [End-to-End Verification of ARM Processors with ISA-Formal]({{ site.url }}/papers/cav2016_isa_formal.pdf), CAV 2016.
* [Verifying against the official ARM specification]({{ site.baseurl }}{% post_url 2016-07-26-using-armarm %})
* [Finding Bugs versus Proving Absence of Bugs]({{ site.baseurl }}{% post_url 2016-07-18-finding-bugs %})
* [Limitations of ISA-Formal]({{ site.baseurl }}{% post_url 2016-07-30-isa-formal-limitations %})
* Paper: [Trustworthy Specifications of ARM v8-A and v8-M System Level Architecture]({{ site.url }}/papers/fmcad2016-trustworthy.pdf)), FMCAD 2016.
* [ARM's ASL Specification Language]({{ site.baseurl }}{% post_url 2016-08-17-specification_languages %})
* [ARM Releases Machine Readable Architecture Specification]({{ site.baseurl }}{% post_url 2017-04-20-ARM-v8a-xml-release %})
* [Dissecting the ARM Machine Readable Architecture files]({{ site.baseurl }}{% post_url 2017-04-29-dissecting-ARM-MRA %})
* Code: [MRA Tools](https://github.com/alastairreid/mra_tools)
* This post: [ASL Lexical Syntax]({{ site.baseurl }}{% post_url 2017-05-07-asl-lexical-syntax %})
* [Arm v8.3 Machine Readable Specifications]({{ site.baseurl }}{% post_url 2017-07-31-arm-v8.3 %})
