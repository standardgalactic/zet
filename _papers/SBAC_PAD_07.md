---
layout: paper
year: 2007
title: Low-cost Techniques for Reducing Branch Context Pollution in a Soft Realtime Embedded Multithreaded Processor
publisher: IEEE Computer Society
png: SBACPAD07.png
pages: 37--44
month: October
location: Gramado, RS, Brazil
file: SBACPAD07.pdf
doi: 10.1109/SBAC-PAD.2007.15
day: 24-27
booktitle: 19th Symposium on Computer Architecture and High Performance Computing (SBAC-PAD 2007)
author: Emre Özer, Alastair Reid, Stuart Biles
ar_shortname: SBAC-PAD 07
ar_file: SBAC_PAD_07
affiliation: ARM Ltd
abstract: |
    
    In this paper, we propose two low-cost and novel branch history
    buffer handling schemes aiming at skewing the branch prediction
    accuracy in favor of a real-time thread for a soft real-time
    embedded multithreaded processor. The processor core accommodates
    two running threads, one with the highest priority and the other
    thread is a background thread, and both threads share the branch
    predictor. The first scheme uses a 3-bit branch history buffer in
    which the highest priority thread uses the most significant
    2 bits to change the prediction state while the background thread
    uses only the least significant 2 bits. The second scheme uses
    the shared 2-bit branch history buffer that implements integer
    updates for the highest priority thread but fractional updates
    for the background thread in order to achieve relatively higher
    prediction accuracy in the highest priority thread. The low cost
    nature of these two schemes, particularly in the second scheme,
    makes them attractive with moderate improvement in the
    performance of the highest priority thread.
ENTRYTYPE: inproceedings
ID: DBLPconf/sbac-pad/OzerRB07
bibtex: |
    @inproceedings{DBLP:conf/sbac-pad/OzerRB07
        , abstract = {
    In this paper, we propose two low-cost and novel branch history
    buffer handling schemes aiming at skewing the branch prediction
    accuracy in favor of a real-time thread for a soft real-time
    embedded multithreaded processor. The processor core accommodates
    two running threads, one with the highest priority and the other
    thread is a background thread, and both threads share the branch
    predictor. The first scheme uses a 3-bit branch history buffer in
    which the highest priority thread uses the most significant
    2 bits to change the prediction state while the background thread
    uses only the least significant 2 bits. The second scheme uses
    the shared 2-bit branch history buffer that implements integer
    updates for the highest priority thread but fractional updates
    for the background thread in order to achieve relatively higher
    prediction accuracy in the highest priority thread. The low cost
    nature of these two schemes, particularly in the second scheme,
    makes them attractive with moderate improvement in the
    performance of the highest priority thread.
    }
        , affiliation = {ARM Ltd}
        , ar_file = {SBAC_PAD_07}
        , ar_shortname = {SBAC-PAD 07}
        , author = {Emre {\"O}zer and
    Alastair Reid and
    Stuart Biles}
        , booktitle = {19th Symposium on Computer Architecture and High Performance Computing
    (SBAC-PAD 2007)}
        , day = {24-27}
        , doi = {10.1109/SBAC-PAD.2007.15}
        , file = {SBACPAD07.pdf}
        , location = {Gramado, RS, Brazil}
        , month = {October}
        , pages = {37--44}
        , png = {SBACPAD07.png}
        , publisher = {IEEE Computer Society}
        , title = {{L}ow-cost {T}echniques for {R}educing {B}ranch {C}ontext {P}ollution in a {S}oft
    {R}ealtime {E}mbedded {M}ultithreaded {P}rocessor}
        , year = {2007}
    }
---
