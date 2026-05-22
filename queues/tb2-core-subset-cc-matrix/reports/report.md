# TB2 Queue Report

Queue: `/root/tb2-claude-bench/queues/tb2-core-subset-cc-matrix`
Dataset: `/root/tb2-claude-bench/data/terminal-bench-2`

# TB2 Queue Summary

Updated: `2026-05-22T07:30:47+00:00`

| Agent | Model | Version | Mode | Done | Passed | Failed | Accuracy | Input Tokens | Cache Tokens | Output Tokens | Total Tokens | Cost USD |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 20/84 | 11 | 9 | 0.550 | 485 | 18997104 | 281491 | 19279080 | 9.488768 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 20/84 | 8 | 12 | 0.400 | 30954004 | 30209442 | 298710 | 61462156 | 13.687168 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 20/84 | 11 | 9 | 0.550 | 26833070 | 25829881 | 56057 | 52719008 | 15.298609 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 20/84 | 7 | 13 | 0.350 | 27277926 | 25401154 | 289155 | 52968235 | 20.137453 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 19/84 | 10 | 9 | 0.526 | 12958122 | 12002958 | 13259 | 24974339 | 18.337322 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 20/84 | 9 | 11 | 0.450 | 11313481 | 10556394 | 14931 | 21884806 | 21.693645 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 19/84 | 6 | 13 | 0.316 | 9599506 | 8906720 | 688664 | 19194890 | 10.753899 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 19/84 | 13 | 6 | 0.684 | 9638909 | 9045559 | 621957 | 19306425 | 11.362326 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 18/84 | 10 | 8 | 0.556 | 7363452 | 6957853 | 497917 | 14819222 | 8.225948 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 18/84 | 11 | 7 | 0.611 | 8834571 | 8312694 | 545182 | 17692447 | 9.144744 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 18/84 | 10 | 8 | 0.556 | 8310154 | 7789999 | 450945 | 16551098 | 8.985198 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 18/84 | 12 | 6 | 0.667 | 8757731 | 8212460 | 589687 | 17559878 | 9.206524 |

## Jobs

| Status | Task | Agent | Model | Version | Mode | Reward | Input Tokens | Cache Tokens | Output Tokens | Total Tokens | Cost USD | Error |
|---|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| completed | adaptive-rejection-sampler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 35 | 1306760 | 30304 | 1337099 | 1.061649 |  |
| completed | adaptive-rejection-sampler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 222134 | 197699 | 9446 | 429279 | 0.292621 |  |
| completed | adaptive-rejection-sampler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 1840541 | 1783068 | 1762 | 3625371 | 1.149541 |  |
| completed | adaptive-rejection-sampler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 462013 | 364165 | 3814 | 829992 | 1.691896 |  |
| completed | adaptive-rejection-sampler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 39719 | 0 | 8 | 39727 |  |  |
| completed | adaptive-rejection-sampler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 242954 | 211690 | 573 | 455217 | 1.565503 |  |
| completed | adaptive-rejection-sampler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 699530 | 664373 | 49351 | 1413254 | 1.071395 |  |
| completed | adaptive-rejection-sampler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 214461 | 167829 | 55662 | 437952 |  |  |
| completed | adaptive-rejection-sampler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 98313 | 81215 | 64299 | 243827 |  |  |
| completed | adaptive-rejection-sampler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 14195 | 8163 | 64348 | 86706 |  |  |
| completed | adaptive-rejection-sampler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 157453 | 138520 | 39049 | 335022 | 0.698281 |  |
| completed | adaptive-rejection-sampler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 14024 | 8124 | 64386 | 86534 |  |  |
| completed | bn-fit-modify | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 16 | 311117 | 6227 | 317360 | 0.234795 |  |
| completed | bn-fit-modify | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 393089 | 369886 | 6998 | 769973 | 0.302930 |  |
| completed | bn-fit-modify | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 777043 | 746083 | 1857 | 1524983 | 0.489179 |  |
| completed | bn-fit-modify | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 1041448 | 973233 | 9385 | 2024066 | 0.770628 |  |
| completed | bn-fit-modify | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 432195 | 417991 | 720 | 850906 | 0.568719 |  |
| completed | bn-fit-modify | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 240736 | 212091 | 512 | 453339 | 0.630291 |  |
| completed | bn-fit-modify | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 301121 | 279912 | 11828 | 592861 | 0.340916 |  |
| completed | bn-fit-modify | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 421716 | 392916 | 14327 | 828959 | 0.440760 |  |
| completed | bn-fit-modify | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 444545 | 422343 | 12364 | 879252 | 0.395405 |  |
| completed | bn-fit-modify | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 82760 | 63941 | 7343 | 154044 | 0.199890 |  |
| completed | bn-fit-modify | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 413353 | 390089 | 13163 | 816605 | 0.401699 |  |
| completed | bn-fit-modify | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 121856 | 98958 | 10418 | 231232 | 0.271815 |  |
| completed | break-filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 2 | 15410 | 41 | 15453 | 0.058409 |  |
| completed | break-filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 13548 | 0 | 34 | 13582 | 0.051314 |  |
| completed | break-filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 3669901 | 3601362 | 4985 | 7276248 | 1.953349 |  |
| completed | break-filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 234473 | 187309 | 603 | 422385 | 0.246140 |  |
| completed | break-filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 1005781 | 830363 | 453 | 1836597 |  |  |
| completed | break-filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 820313 | 759723 | 665 | 1580701 | 1.931229 |  |
| completed | break-filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 301641 | 242674 | 66853 | 611168 |  |  |
| completed | break-filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 473516 | 433026 | 30845 | 937387 | 0.744408 |  |
| completed | break-filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 50571 | 37042 | 64158 | 151771 |  |  |
| completed | break-filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 342604 | 308160 | 28875 | 679639 | 0.654727 |  |
| completed | break-filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 183242 | 138920 | 63357 | 385519 |  |  |
| completed | break-filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 936888 | 858805 | 68782 | 1864475 |  |  |
| completed | build-cython-ext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 40 | 4791960 | 11742 | 4803742 | 2.129347 |  |
| completed | build-cython-ext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 4106648 | 4046829 | 16771 | 8170248 | 1.689859 |  |
| completed | build-cython-ext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 4509187 | 4436348 | 3085 | 8948620 | 1.842657 |  |
| completed | build-cython-ext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 3706469 | 3569786 | 3436 | 7279691 | 1.672254 |  |
| completed | build-cython-ext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 3422310 | 3365738 | 2689 | 6790737 | 2.674062 |  |
| completed | build-cython-ext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 3408243 | 3342089 | 2980 | 6753312 | 2.696253 |  |
| completed | build-cython-ext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 1050400 | 1018236 | 8994 | 2077630 | 0.559365 |  |
| completed | build-cython-ext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 2601553 | 2549112 | 14967 | 5165632 | 1.184653 |  |
| completed | build-cython-ext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 1353744 | 1316098 | 10977 | 2680819 | 0.769664 |  |
| completed | build-cython-ext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 2674023 | 2614432 | 19577 | 5308032 | 1.296520 |  |
| completed | build-cython-ext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 1494177 | 1443104 | 13119 | 2950400 | 0.819902 |  |
| completed | build-cython-ext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 2610341 | 2548325 | 20751 | 5179417 | 1.301679 |  |
| completed | build-pov-ray | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 59 | 2083446 | 13637 | 2097142 | 1.027323 |  |
| completed | build-pov-ray | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 1165560 | 1106718 | 7269 | 2279547 | 0.933347 |  |
| completed | build-pov-ray | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 611497 | 580954 | 1085 | 1193536 | 0.421033 |  |
| completed | build-pov-ray | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 531529 | 476185 | 1431 | 1009145 | 0.475459 |  |
| completed | build-pov-ray | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 2273393 | 2231784 | 2043 | 4507220 | 1.780734 |  |
| completed | build-pov-ray | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 855889 | 826512 | 1407 | 1683808 | 0.839317 |  |
| completed | build-pov-ray | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 424453 | 404655 | 3376 | 832484 | 0.323484 |  |
| completed | build-pov-ray | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 855492 | 823868 | 7991 | 1687351 | 0.485063 |  |
| completed | build-pov-ray | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 517705 | 493036 | 4182 | 1014923 | 0.290493 |  |
| completed | build-pov-ray | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 465182 | 438955 | 6331 | 910468 | 0.324982 |  |
| completed | build-pov-ray | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 1477602 | 1442286 | 9219 | 2929107 | 0.703372 |  |
| completed | build-pov-ray | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 193917 | 177672 | 3060 | 374649 | 0.160107 |  |
| completed | caffe-cifar-10 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 37 | 767607 | 4833 | 772477 |  |  |
| completed | caffe-cifar-10 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 3399644 | 3367082 | 17499 | 6784225 |  |  |
| completed | caffe-cifar-10 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 900739 | 841060 | 2529 | 1744328 |  |  |
| completed | caffe-cifar-10 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 860881 | 774046 | 3558 | 1638485 |  |  |
| completed | caffe-cifar-10 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 761472 | 719940 | 1548 | 1482960 |  |  |
| completed | caffe-cifar-10 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 332153 | 302171 | 1020 | 635344 |  |  |
| completed | caffe-cifar-10 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 15743 | 10676 | 1456 | 27875 |  |  |
| completed | caffe-cifar-10 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 492193 | 474223 | 6293 | 972709 |  |  |
| completed | caffe-cifar-10 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 571946 | 541232 | 5044 | 1118222 |  |  |
| completed | caffe-cifar-10 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 574492 | 534689 | 8491 | 1117672 |  |  |
| completed | caffe-cifar-10 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 596562 | 552468 | 4701 | 1153731 |  |  |
| completed | caffe-cifar-10 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 812804 | 764678 | 16004 | 1593486 |  |  |
| completed | cancel-async-tasks | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 3 | 31260 | 298 | 31561 | 0.017103 |  |
| completed | cancel-async-tasks | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 27511 | 13522 | 275 | 41308 | 0.060638 |  |
| completed | cancel-async-tasks | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 29294 | 14523 | 60 | 43877 | 0.064111 |  |
| completed | cancel-async-tasks | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 60841 | 17604 | 69 | 78514 | 0.150033 |  |
| completed | cancel-async-tasks | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 41587 | 19359 | 9 | 60955 | 0.226351 |  |
| completed | cancel-async-tasks | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 66748 | 54488 | 125 | 121361 | 0.276693 |  |
| completed | cancel-async-tasks | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 33346 | 26390 | 2000 | 61736 | 0.064000 |  |
| completed | cancel-async-tasks | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 46536 | 36921 | 4275 | 87732 | 0.111252 |  |
| completed | cancel-async-tasks | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 33890 | 26356 | 2795 | 63041 | 0.078082 |  |
| completed | cancel-async-tasks | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 9778 | 6357 | 3107 | 19242 | 0.061338 |  |
| completed | cancel-async-tasks | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 36274 | 29096 | 2058 | 67428 | 0.066514 |  |
| completed | cancel-async-tasks | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 26789 | 18961 | 5797 | 51547 | 0.121994 |  |
| completed | chess-best-move | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 4 | 49479 | 1144 | 50627 | 0.092649 |  |
| completed | chess-best-move | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 1706280 | 1648777 | 36540 | 3391597 | 1.258332 |  |
| completed | chess-best-move | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 1149565 | 1095056 | 2519 | 2247140 |  |  |
| completed | chess-best-move | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 508828 | 407693 | 8588 | 925109 | 0.810402 |  |
| completed | chess-best-move | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 39268 | 19301 | 16 | 58585 |  |  |
| completed | chess-best-move | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 632768 | 578347 | 539 | 1211654 | 1.682067 |  |
| completed | chess-best-move | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 80883 | 53374 | 48375 | 182632 | 0.844791 |  |
| completed | chess-best-move | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 340903 | 302203 | 17994 | 661100 | 0.505683 |  |
| completed | chess-best-move | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 31916 | 26298 | 32113 | 90327 |  |  |
| completed | chess-best-move | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 25592 | 17727 | 35953 | 79272 |  |  |
| completed | chess-best-move | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 34924 | 29038 | 32115 | 96077 |  |  |
| completed | chess-best-move | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 228959 | 170161 | 43079 | 442199 |  |  |
| completed | circuit-fibsqrt | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 27 | 1303701 | 43272 | 1347000 | 1.281509 |  |
| completed | circuit-fibsqrt | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 59924 | 36700 | 20276 | 116900 | 0.402237 |  |
| completed | circuit-fibsqrt | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 1048888 | 986750 | 480 | 2036118 | 1.130237 |  |
| completed | circuit-fibsqrt | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 6440963 | 6106181 | 103830 | 12650974 | 5.783906 |  |
| completed | circuit-fibsqrt | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 117227 | 19523 | 25 | 136775 | 3.823947 |  |
| completed | circuit-fibsqrt | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 45222 | 5122 | 16 | 50360 | 3.456696 |  |
| completed | circuit-fibsqrt | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 96926 | 58582 | 128153 | 283661 | 2.083405 |  |
| completed | circuit-fibsqrt | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 42540 | 5008 | 128144 | 175692 | 2.064152 |  |
| completed | circuit-fibsqrt | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 97160 | 58548 | 128252 | 283960 | 2.085884 |  |
| completed | circuit-fibsqrt | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 26467 | 1795 | 128142 | 156404 | 2.014934 |  |
| completed | circuit-fibsqrt | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 104283 | 64999 | 128156 | 297438 | 2.088900 |  |
| completed | circuit-fibsqrt | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 26412 | 3926 | 128157 | 158495 | 2.007600 |  |
| completed | cobol-modernization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 15 | 334768 | 4184 | 338967 | 0.258807 |  |
| completed | cobol-modernization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 616182 | 586536 | 8781 | 1211499 | 0.418787 |  |
| completed | cobol-modernization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 669090 | 637143 | 1871 | 1308104 | 0.484302 |  |
| completed | cobol-modernization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 734539 | 676458 | 1828 | 1412825 | 0.610605 |  |
| completed | cobol-modernization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 745823 | 696803 | 556 | 1443182 | 1.277899 |  |
| completed | cobol-modernization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 687157 | 641794 | 721 | 1329672 | 1.422976 |  |
| completed | cobol-modernization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 699099 | 639150 | 33318 | 1371567 | 0.916309 |  |
| completed | cobol-modernization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 1315758 | 1261289 | 39324 | 2616371 | 1.172476 |  |
| completed | cobol-modernization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 468392 | 438755 | 20355 | 927502 | 0.548027 |  |
| completed | cobol-modernization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 321011 | 284155 | 27698 | 632864 | 0.638914 |  |
| completed | cobol-modernization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 578247 | 536947 | 31264 | 1146458 | 0.784856 |  |
| completed | cobol-modernization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 394708 | 359921 | 27462 | 782091 | 0.650342 |  |
| completed | code-from-image | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 4 | 51467 | 272 | 51743 | 0.082257 |  |
| completed | code-from-image | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 45882 | 29558 | 303 | 75743 | 0.074624 |  |
| completed | code-from-image | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 46258 | 30246 | 107 | 76611 | 0.073151 |  |
| completed | code-from-image | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 100438 | 55657 | 11 | 156106 | 0.172030 |  |
| completed | code-from-image | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 82470 | 61130 | 18 | 143618 | 0.188621 |  |
| completed | code-from-image | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 24985 | 17936 | 57 | 42978 | 0.079793 |  |
| completed | code-from-image | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 50240 | 43341 | 643 | 94224 | 0.048516 |  |
| completed | code-from-image | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 17719 | 15230 | 994 | 33943 | 0.028810 |  |
| completed | code-from-image | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 68152 | 60969 | 968 | 130089 | 0.059743 |  |
| completed | code-from-image | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 8011 | 5591 | 877 | 14479 | 0.023904 |  |
| completed | code-from-image | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 54730 | 47522 | 765 | 103017 | 0.052759 |  |
| completed | code-from-image | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 8048 | 5537 | 1001 | 14586 | 0.026089 |  |
| completed | compile-compcert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 60 | 1570295 | 7972 | 1578327 | 1.048091 |  |
| completed | compile-compcert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 13009466 | 12942735 | 39479 | 25991680 | 4.725035 |  |
| completed | compile-compcert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 1585846 | 1511014 | 3015 | 3099875 |  |  |
| completed | compile-compcert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 2460115 | 2406253 | 5880 | 4872248 |  |  |
| completed | compile-compcert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 1502949 | 1406236 | 1593 | 2910778 | 1.543989 |  |
| completed | compile-compcert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 589273 | 523028 | 1427 | 1113728 |  |  |
| completed | compile-compcert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 872826 | 807503 | 9394 | 1689723 |  |  |
| completed | compile-compcert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 1378295 | 1336351 | 18960 | 2733606 | 0.842548 |  |
| completed | compile-compcert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 1302829 | 1270882 | 15200 | 2588911 | 0.729033 |  |
| completed | compile-compcert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 1135807 | 1059869 | 15619 | 2211295 | 0.836717 |  |
| completed | compile-compcert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 1755170 | 1650100 | 13135 | 3418405 | 1.085576 |  |
| completed | compile-compcert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 1041625 | 979016 | 16969 | 2037610 | 0.782980 |  |
| completed | configure-git-webserver | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 19 | 303861 | 2021 | 305901 | 0.185873 |  |
| completed | configure-git-webserver | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 276709 | 259696 | 2344 | 538749 | 0.176853 |  |
| completed | configure-git-webserver | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 407258 | 401672 | 1218 | 810148 | 0.193110 |  |
| completed | configure-git-webserver | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 313249 | 266705 | 2310 | 582264 | 0.278889 |  |
| completed | configure-git-webserver | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 518214 | 492749 | 786 | 1011749 | 0.572704 |  |
| completed | configure-git-webserver | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 169988 | 158762 | 1109 | 329859 | 0.267192 |  |
| completed | configure-git-webserver | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 538170 | 526491 | 4274 | 1068935 | 0.265806 |  |
| completed | configure-git-webserver | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 139830 | 128051 | 4521 | 272402 | 0.150388 |  |
| completed | configure-git-webserver | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 294247 | 284291 | 3534 | 582072 | 0.175620 |  |
| completed | configure-git-webserver | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 72929 | 65881 | 4419 | 143229 | 0.112467 |  |
| completed | configure-git-webserver | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 300619 | 290178 | 4313 | 595110 | 0.190890 |  |
| completed | configure-git-webserver | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 87337 | 79291 | 4355 | 170983 | 0.119270 |  |
| completed | constraints-scheduling | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 4 | 59481 | 2554 | 62039 | 0.134778 |  |
| completed | constraints-scheduling | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 53128 | 33003 | 1578 | 87709 | 0.109037 |  |
| completed | constraints-scheduling | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 108735 | 89129 | 140 | 198004 | 0.132836 |  |
| completed | constraints-scheduling | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 143172 | 93312 | 5125 | 241609 | 0.300119 |  |
| completed | constraints-scheduling | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 158662 | 129127 | 91 | 287880 | 0.433849 |  |
| completed | constraints-scheduling | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 69855 | 55042 | 140 | 125037 | 0.277081 |  |
| completed | constraints-scheduling | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 60235 | 44189 | 7328 | 111752 | 0.182418 |  |
| completed | constraints-scheduling | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 119648 | 102949 | 10523 | 233120 | 0.250416 |  |
| completed | constraints-scheduling | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 93903 | 73519 | 10338 | 177760 | 0.279113 |  |
| completed | constraints-scheduling | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 62941 | 48639 | 10573 | 122153 | 0.226814 |  |
| completed | constraints-scheduling | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 62035 | 49603 | 4715 | 116353 | 0.132223 |  |
| completed | constraints-scheduling | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 57300 | 44909 | 8319 | 110528 | 0.184719 |  |
| completed | count-dataset-tokens | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 24 | 714576 | 7036 | 721636 | 0.418969 |  |
| completed | count-dataset-tokens | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 203325 | 182288 | 2021 | 387634 | 0.229732 |  |
| completed | count-dataset-tokens | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 393600 | 377221 | 700 | 771521 | 0.224689 |  |
| completed | count-dataset-tokens | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 200775 | 161715 | 1452 | 363942 | 0.272938 |  |
| completed | count-dataset-tokens | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 324769 | 316650 | 426 | 641845 | 0.344862 |  |
| completed | count-dataset-tokens | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 124870 | 112945 | 307 | 238122 | 0.309732 |  |
| completed | count-dataset-tokens | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 183046 | 173949 | 2100 | 359095 | 0.126954 |  |
| completed | count-dataset-tokens | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 116150 | 98763 | 6523 | 221436 | 0.192667 |  |
| completed | count-dataset-tokens | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 163261 | 153865 | 2339 | 319465 | 0.124900 |  |
| completed | count-dataset-tokens | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 444187 | 418614 | 15455 | 878256 | 0.453285 |  |
| completed | count-dataset-tokens | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 179228 | 169030 | 2924 | 351182 | 0.140867 |  |
| completed | count-dataset-tokens | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 67218 | 55780 | 3601 | 126599 | 0.113634 |  |
| completed | crack-7z-hash | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 30 | 1046940 | 4380 | 1051350 | 0.474557 |  |
| completed | crack-7z-hash | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 1607962 | 1578295 | 4999 | 3191256 | 0.659690 |  |
| completed | crack-7z-hash | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 757106 | 744004 | 1775 | 1502885 | 0.356409 |  |
| completed | crack-7z-hash | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 4435770 | 4341376 | 29211 | 8806357 | 2.486866 |  |
| completed | crack-7z-hash | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 1018797 | 1005393 | 1855 | 2026045 | 0.812487 |  |
| completed | crack-7z-hash | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 1453401 | 1395481 | 1635 | 2850517 | 2.057854 |  |
| completed | crack-7z-hash | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 2768101 | 2656090 | 46492 | 5470683 | 1.914201 |  |
| completed | crack-7z-hash | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 521459 | 499729 | 9157 | 1030345 | 0.368727 |  |
| completed | crack-7z-hash | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 713747 | 698206 | 6323 | 1418276 | 0.362559 |  |
| completed | crack-7z-hash | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 666550 | 624719 | 19518 | 1310787 | 0.637016 |  |
| completed | crack-7z-hash | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 525726 | 512188 | 3109 | 1041023 | 0.251039 |  |
| completed | crack-7z-hash | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 2030495 | 1958598 | 33889 | 4022982 | 1.365472 |  |
| completed | db-wal-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 49 | 2519520 | 53031 | 2572600 |  |  |
| completed | db-wal-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 953479 | 894739 | 15082 | 1863300 | 1.164791 |  |
| completed | db-wal-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 3595681 | 3527540 | 3479 | 7126700 | 1.772998 |  |
| completed | db-wal-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 2624091 | 2539459 | 14370 | 5177920 | 1.828331 |  |
| completed | db-wal-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 279073 | 251139 | 399 | 530611 | 0.398977 |  |
| completed | db-wal-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 935689 | 861714 | 720 | 1798123 |  |  |
| completed | db-wal-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 1128248 | 1064855 | 50813 | 2243916 |  |  |
| completed | db-wal-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 159539 | 142586 | 5251 | 307376 | 0.185105 |  |
| completed | db-wal-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 166272 | 153363 | 2283 | 321918 | 0.128656 |  |
| completed | db-wal-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 1854397 | 1775263 | 43163 | 3672823 |  |  |
| completed | db-wal-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 164442 | 148857 | 3496 | 316795 | 0.155535 |  |
| completed | db-wal-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 91520 | 79798 | 5657 | 176975 | 0.152744 |  |
| completed | distribution-search | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 24 | 682834 | 23285 | 706143 | 0.656386 |  |
| completed | distribution-search | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 347309 | 319405 | 11885 | 678599 | 0.378724 |  |
| completed | distribution-search | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 1403751 | 1341712 | 2091 | 2747554 | 1.143422 |  |
| completed | distribution-search | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 921650 | 786996 | 15587 | 1724233 | 1.303228 |  |
| completed | distribution-search | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 78422 | 0 | 8 | 78430 | 3.690124 |  |
| completed | distribution-search | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 20818 | 4427 | 22 | 25267 | 3.304644 |  |
| completed | distribution-search | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 63914 | 42704 | 128000 | 234618 | 2.012340 |  |
| completed | distribution-search | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 346977 | 265975 | 150112 | 763064 | 2.635216 |  |
| completed | distribution-search | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 892859 | 821835 | 112393 | 1827087 | 2.198767 |  |
| completed | distribution-search | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 53645 | 35744 | 105693 | 195082 | 1.663236 |  |
| completed | distribution-search | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 192087 | 157054 | 82287 | 431428 | 1.412786 |  |
| completed | distribution-search | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 7490 | 0 | 128000 | 135490 | 1.948079 |  |
| completed | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 18 | 663016 | 58873 | 721907 |  |  |
| completed | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 1568410 | 1462334 | 80270 | 3111014 |  |  |
| completed | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 2311597 | 2143961 | 22515 | 4478073 | 2.676712 |  |
| completed | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 935994 | 789826 | 55718 | 1781538 |  |  |
| completed | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 115991 | 19732 | 16 | 135739 |  |  |
| completed | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 186780 | 125279 | 461 | 312520 |  |  |
| completed | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 231584 | 149576 | 85916 | 467076 |  |  |
| completed | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 34624 | 9530 | 96094 | 140248 |  |  |
| running | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| running | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| running | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| running | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 15 | 389606 | 6385 | 396006 | 0.326265 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 1177814 | 1133640 | 16860 | 2328314 | 0.758618 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 1017493 | 941035 | 784 | 1959312 | 1.190873 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 560688 | 407195 | 22949 | 990832 | 1.283730 |  |
| running | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 405639 | 367753 | 495 | 773887 | 0.896324 |  |
| running | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| running | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | sparql-university | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | sparql-university | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | sparql-university | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | sparql-university | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | sparql-university | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | sparql-university | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | sparql-university | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | sparql-university | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | sparql-university | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | sparql-university | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | sparql-university | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | sparql-university | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | sqlite-db-truncate | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | sqlite-db-truncate | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | sqlite-db-truncate | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | sqlite-db-truncate | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | sqlite-db-truncate | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | sqlite-db-truncate | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | sqlite-db-truncate | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | sqlite-db-truncate | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | sqlite-db-truncate | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | sqlite-db-truncate | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | sqlite-db-truncate | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | sqlite-db-truncate | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | sqlite-with-gcov | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | sqlite-with-gcov | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | sqlite-with-gcov | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | sqlite-with-gcov | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | sqlite-with-gcov | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | sqlite-with-gcov | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | sqlite-with-gcov | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | sqlite-with-gcov | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | sqlite-with-gcov | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | sqlite-with-gcov | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | sqlite-with-gcov | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | sqlite-with-gcov | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | torch-pipeline-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | torch-pipeline-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | torch-pipeline-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | torch-pipeline-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | torch-pipeline-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | torch-pipeline-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | torch-pipeline-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | torch-pipeline-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | torch-pipeline-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | torch-pipeline-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | torch-pipeline-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | torch-pipeline-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | torch-tensor-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | torch-tensor-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | torch-tensor-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | torch-tensor-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | torch-tensor-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | torch-tensor-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | torch-tensor-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | torch-tensor-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | torch-tensor-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | torch-tensor-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | torch-tensor-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | torch-tensor-parallelism | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | train-fasttext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | train-fasttext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | train-fasttext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | train-fasttext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | train-fasttext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | train-fasttext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | train-fasttext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | train-fasttext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | train-fasttext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | train-fasttext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | train-fasttext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | train-fasttext | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | tune-mjcf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | tune-mjcf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | tune-mjcf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | tune-mjcf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | tune-mjcf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | tune-mjcf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | tune-mjcf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | tune-mjcf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | tune-mjcf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | tune-mjcf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | tune-mjcf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | tune-mjcf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | video-processing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | video-processing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | video-processing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | video-processing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | video-processing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | video-processing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | video-processing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | video-processing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | video-processing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | video-processing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | video-processing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | video-processing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | vulnerable-secret | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | vulnerable-secret | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | vulnerable-secret | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | vulnerable-secret | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | vulnerable-secret | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | vulnerable-secret | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | vulnerable-secret | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | vulnerable-secret | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | vulnerable-secret | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | vulnerable-secret | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | vulnerable-secret | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | vulnerable-secret | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | winning-avg-corewars | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | winning-avg-corewars | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | winning-avg-corewars | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | winning-avg-corewars | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | winning-avg-corewars | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | winning-avg-corewars | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | winning-avg-corewars | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | winning-avg-corewars | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | winning-avg-corewars | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | winning-avg-corewars | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | winning-avg-corewars | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | winning-avg-corewars | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
| queued | write-compressor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular |  |  |  |  |  |  |  |
| queued | write-compressor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular |  |  |  |  |  |  |  |
| queued | write-compressor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular |  |  |  |  |  |  |  |
| queued | write-compressor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular |  |  |  |  |  |  |  |
| queued | write-compressor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| queued | write-compressor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| queued | write-compressor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| queued | write-compressor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| queued | write-compressor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| queued | write-compressor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| queued | write-compressor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
| queued | write-compressor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple |  |  |  |  |  |  |  |
