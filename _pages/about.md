---
permalink: /
title: "About"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Leeor Peled has over 20 years of experience developing CPU core architectures, starting at Intel working on various cores from Sandybridge, Ivybridge & Skylake, until Goldencove and Lioncove.
He then moved to Huawei as a senior architect and research manager working on CPU cores for Mobile phones, server CPUs and many other domains. Leeor received his PhD at the Technion under Prof. [Uri Weiser](http://webee.technion.ac.il/people/weiser) & Prof. [Yoav Etsion](http://www.cs.technion.ac.il/~yetsion/).

Currently he is leading Huawei CPU Architecture Research with a team that spans across Israel, Zurich, Cambridge, Edinburgh, and China. His main focus is on Predictors, Parallelism, Caches, Software/Hardware codesign, System/OS, and dynamic optimization, but he may be willing to talk about other things if you're not careful. He also serves as an associate editor of IEEE Computer Architecture Letters (CAL) and PC memeber on recent ISCA, Micro and HPCA conferences.

Fun fact: likes windsurfing :)

---------

Areas of Interest
=======
- CPU Architecture and Microarchitecture (uArch)
- Predictors, prefetchers and adaptive configurability
- Automated parallelism
- Code semantics inference and extrpolation
- Hardware-Software Codesign
- Memory Hierarchy: Prefetching and Cache Design, replacement policies
- Machine Learning for CPU optimization
- Performance evaluation, modeling and reliable benchmarking
- Binary translation and optimization (BT/DBO)
- Transactional Memory


------

Employment
=====
- 2005 - 2020: Performance Architect at Intel, focusing on CPU microarchitecture design and optimization
  
  ![Intel logo2](images/image-20-600x338.png[1].webp)

- 2020 - 2023: Senior Architect at Huawei (Toga Networks - Israel research center), head of Advanced Technologies Group (ATG)
- 2023 - 2026: Head of CPU Architecture Research at Huawei (Skyline CPU)
  
  ![Huawei logo](images/Huawei-Logo-500x281.png)

-----

Publications (see extended version through tabs)
========
{% assign pubs = site.data.publications | sort: 'date'  %}
{% for p in pubs %}
- {% if p.pub_date %}{{ p.pub_date | pub_date: "%Y" }}{% else %}n.d.{% endif %} — {% if p.venue %}{{ p.venue }}{% else %}Unknown venue{% endif %} — {% if p.url %}[{{ p.title }}]({{ p.url }}){% else %}{{ p.title }}{% endif %}
{% endfor %}

Invited talks
=====
- Recent directions in CPU Architecture, talk at Bar-Ilan university [Link]
- DPC4 [Talk](https://sites.google.com/view/dpc4-2026/program/invited-talks), [Full recording](https://www.youtube.com/watch?v=kGof6AnzICs)
- Future of CPU research in the agentic AI, Tech talks [Link]

-----

Service
======
- Conferences:
    - [CATC - Compilers, Architecture and Tools Conference](https://software.intel.com/en-us/event/compilerconf/2015/sessions) (Co-organizer and Program Committee
    - [Micro 56](http://www.microarch.org/micro56/) - 56th IEEE/ACM International Symposium on Microarchitecture 2023 (Toronto) - Program committee
    - [Micro 57](http://www.microarch.org/micro57) - 56th IEEE/ACM International Symposium on Microarchitecture 2024 (Austin) - Program committee
    - [Micro 58](http://www.microarch.org/micro58) - 56th IEEE/ACM International Symposium on Microarchitecture 2025 (Seoul) - Program committee
    - [ISCA 2016](https://www.iscaconf.org/isca2016) - International Symposium on Computer Architecture (Seoul) - ERC
    - [ISCA 2022](https://www.iscaconf.org/isca2022) - 49th IEEE/ACM International Symposium on Computer Architecture (NY) - ERC
    - [ISCA 2026](https://www.iscaconf.org/isca2026) - 53rd IEEE/ACM International Symposium on Computer Architecture (Raleigh) - ERC
    - [HPCA 2026](https://2026.hpca-conf.org) - 32st IEEE International Symposium on High-Performance Computer Architecture (Sydney) - Program committee
    - [HPCA 2027](https://2027.hpca-conf.org) - 33st IEEE International Symposium on High-Performance Computer Architecture (Salt Lake City) - Program committee
    - [DPC 4](https://sites.google.com/view/dpc4-2026) - 4th Data Prefetching Championship (in conjunction with HPCA 2026) - Program committee,

- Journals:
    - Associate editor for [IEEE Computer Architecture Letters (CAL)](https://www.computer.org/csdl/journal/ca)
    - Reviews for TC, TACO, CAL, ICSEE
