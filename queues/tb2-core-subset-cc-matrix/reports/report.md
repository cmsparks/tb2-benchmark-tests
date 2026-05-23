# TB2 Queue Report

Queue: `/root/tb2-claude-bench/queues/tb2-core-subset-cc-matrix`
Dataset: `/root/tb2-claude-bench/data/terminal-bench-2`

# TB2 Queue Summary

Updated: `2026-05-22T23:59:34+00:00`

| Agent | Model | Version | Mode | Done | Passed | Failed | Accuracy | Input Tokens | Cache Tokens | Output Tokens | Total Tokens | Cost USD |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 73/84 | 33 | 40 | 0.452 | 1916 | 103069134 | 1168398 | 104239448 | 42.233661 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 73/84 | 34 | 39 | 0.466 | 152960795 | 149204842 | 1432686 | 303598323 | 49.716896 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 73/84 | 38 | 35 | 0.521 | 90211186 | 86511174 | 177541 | 176899901 | 42.014310 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 73/84 | 29 | 44 | 0.397 | 105421125 | 98367856 | 871717 | 204660698 | 55.816979 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 72/84 | 32 | 40 | 0.444 | 48255327 | 44564807 | 46317 | 92866451 | 55.646835 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 72/84 | 33 | 39 | 0.458 | 54177854 | 50480639 | 48834 | 104707327 | 62.310181 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 72/84 | 26 | 46 | 0.361 | 44153817 | 41422344 | 2154711 | 87730872 | 37.996755 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 72/84 | 36 | 36 | 0.500 | 42997082 | 40007102 | 2157904 | 85162088 | 31.041405 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 72/84 | 34 | 38 | 0.472 | 41434029 | 38875945 | 1958122 | 82268096 | 34.426171 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 72/84 | 34 | 38 | 0.472 | 47114548 | 44004313 | 2187567 | 93306428 | 32.040221 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 72/84 | 33 | 39 | 0.458 | 39221387 | 36922722 | 1791882 | 77935991 | 30.776442 |
| versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 72/84 | 33 | 39 | 0.458 | 39803014 | 36575602 | 2321423 | 78700039 | 30.926428 |

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
| completed | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 79934 | 48081 | 96194 | 224209 |  |  |
| completed | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 21766 | 2004 | 96116 | 119886 |  |  |
| completed | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 87425 | 53295 | 96195 | 236915 |  |  |
| completed | dna-assembly | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 930617 | 697806 | 99912 | 1728335 | 2.581050 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 15 | 389606 | 6385 | 396006 | 0.326265 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 1177814 | 1133640 | 16860 | 2328314 | 0.758618 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 1017493 | 941035 | 784 | 1959312 | 1.190873 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 560688 | 407195 | 22949 | 990832 | 1.283730 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 964766 | 871272 | 799 | 1836837 | 2.812065 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 405639 | 367753 | 495 | 773887 | 0.896324 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 490180 | 448235 | 30110 | 968525 | 0.743403 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 548534 | 499242 | 27908 | 1075684 | 0.753223 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 540287 | 492426 | 33442 | 1066155 | 0.828825 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 221830 | 193299 | 16889 | 432018 | 0.418305 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 417585 | 384847 | 17446 | 819878 | 0.499900 |  |
| completed | dna-insert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 204704 | 176534 | 15915 | 397153 | 0.397311 |  |
| completed | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 18 | 341620 | 4675 | 346313 | 0.258929 |  |
| completed | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 110109 | 92184 | 1003 | 203296 | 0.109913 |  |
| completed | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 187218 | 164808 | 397 | 352423 | 0.169607 |  |
| completed | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 200895 | 140276 | 334 | 341505 | 0.371750 |  |
| completed | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 256762 | 238464 | 247 | 495473 | 0.503174 |  |
| completed | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 346329 | 313442 | 378 | 660149 | 0.925701 |  |
| completed | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 146979 | 132317 | 7580 | 286876 | 0.208372 |  |
| completed | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 372090 | 341754 | 20212 | 734056 | 0.519450 |  |
| completed | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 228276 | 207080 | 11179 | 446535 | 0.309287 |  |
| completed | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 165466 | 143244 | 17287 | 325997 | 0.385600 |  |
| completed | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 254296 | 224440 | 13359 | 492095 | 0.379670 |  |
| completed | extract-elf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 133779 | 118177 | 9804 | 261760 | 0.241010 |  |
| completed | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 2 | 15334 | 85 | 15421 | 0.015448 |  |
| completed | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 41172 | 37119 | 362 | 78653 | 0.071433 |  |
| completed | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 29081 | 14471 | 48 | 43600 | 0.063146 |  |
| completed | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 175619 | 139485 | 914 | 316018 | 0.287053 |  |
| completed | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 164847 | 160914 | 56 | 325817 | 0.181588 |  |
| completed | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 6522362 | 6396024 | 710 | 12919096 |  |  |
| completed | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 3531718 | 3423220 | 68485 | 7023423 | 3.100908 |  |
| completed | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 5925463 | 5805109 | 73922 | 11804494 |  |  |
| completed | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 1686020 | 1614076 | 39566 | 3339662 | 2.042113 |  |
| completed | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 9598899 | 9446621 | 78605 | 19124125 |  |  |
| completed | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 314921 | 303793 | 3195 | 621909 | 0.180769 |  |
| completed | extract-moves-from-video | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 4504694 | 4403195 | 72401 | 8980290 |  |  |
| completed | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 20 | 617649 | 26428 | 644097 | 0.743700 |  |
| completed | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 1649296 | 1573949 | 43526 | 3266771 | 1.542626 |  |
| completed | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 131645 | 107943 | 175 | 239763 |  |  |
| completed | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 624552 | 505042 | 14871 | 1144465 | 1.018754 |  |
| completed | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 552042 | 424615 | 205 | 976862 | 3.586222 |  |
| completed | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 23703 | 13821 | 22 | 37546 |  |  |
| completed | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 83227 | 58427 | 128101 | 269755 | 2.032034 |  |
| completed | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 400521 | 350313 | 68451 | 819285 | 1.320127 |  |
| completed | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 66192 | 47717 | 96114 | 210023 |  |  |
| completed | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 216646 | 177481 | 34442 | 428569 | 0.716736 |  |
| completed | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 286764 | 237476 | 61468 | 585708 | 1.201839 |  |
| completed | feal-differential-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 9871 | 2694 | 96102 | 108667 |  |  |
| completed | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 8 | 191540 | 82274 | 273822 |  |  |
| completed | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 3169120 | 3064822 | 67642 | 6301584 | 2.325163 |  |
| completed | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 652486 | 592521 | 421 | 1245428 | 1.013036 |  |
| completed | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 746153 | 620670 | 51434 | 1418257 |  |  |
| completed | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 119954 | 42996 | 68 | 163018 |  |  |
| completed | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 48021 | 14212 | 68 | 62301 |  |  |
| completed | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 99215 | 65431 | 96258 | 260904 |  |  |
| completed | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 44825 | 13539 | 96248 | 154612 |  |  |
| completed | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 99830 | 67310 | 96322 | 263462 |  |  |
| completed | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 298220 | 229595 | 76734 | 604549 | 1.475808 |  |
| completed | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 106704 | 74002 | 96293 | 276999 |  |  |
| completed | feal-linear-cryptanalysis | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 25676 | 5182 | 96331 | 127189 |  |  |
| completed | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 3 | 31554 | 445 | 32002 | 0.071906 |  |
| completed | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 27819 | 13529 | 463 | 41811 | 0.064589 |  |
| completed | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 29615 | 14530 | 59 | 44204 | 0.070615 |  |
| completed | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 289798 | 191892 | 10722 | 492412 | 1.154105 |  |
| completed | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 47423 | 19366 | 9 | 66798 | 0.407161 |  |
| completed | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 332396 | 287694 | 131 | 620221 | 1.238027 |  |
| completed | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 37377 | 26397 | 6116 | 69890 | 0.140832 |  |
| completed | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 107260 | 86610 | 13952 | 207822 | 0.312695 |  |
| completed | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 65451 | 50871 | 9597 | 125919 | 0.213888 |  |
| completed | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 249611 | 220472 | 19480 | 489563 | 0.467603 |  |
| completed | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 124619 | 107353 | 11504 | 243476 | 0.269509 |  |
| completed | filter-js-from-html | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 58465 | 43591 | 12386 | 114442 | 0.254640 |  |
| completed | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 21 | 1587136 | 5717 | 1592874 | 0.860408 |  |
| completed | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 706085 | 660507 | 5262 | 1371854 | 0.442261 |  |
| completed | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 611722 | 570096 | 747 | 1182565 | 0.518297 |  |
| completed | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 619790 | 542164 | 2271 | 1164225 | 0.538669 |  |
| completed | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 1845890 | 1773594 | 1366 | 3620850 | 1.586066 |  |
| completed | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 425691 | 360100 | 479 | 786270 | 0.938742 |  |
| completed | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 258180 | 212571 | 7111 | 477862 | 0.341461 |  |
| completed | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 204908 | 162596 | 9026 | 376530 | 0.342831 |  |
| completed | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 325259 | 279249 | 7875 | 612383 | 0.374429 |  |
| completed | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 1036689 | 973493 | 22439 | 2032621 | 0.863636 |  |
| completed | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 456123 | 416367 | 6686 | 879176 | 0.374272 |  |
| completed | financial-document-processor | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 216340 | 178736 | 8920 | 403996 | 0.328377 |  |
| completed | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 22 | 626816 | 3385 | 630223 | 0.743914 |  |
| completed | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 952872 | 916515 | 5802 | 1875189 | 0.544802 |  |
| completed | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 615337 | 595131 | 884 | 1211352 | 0.310003 |  |
| completed | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 2134753 | 2011601 | 2048 | 4148402 | 0.824986 |  |
| completed | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 2383693 | 2277536 | 1385 | 4662614 | 1.996626 |  |
| completed | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 1423028 | 1333234 | 902 | 2757164 | 1.419068 |  |
| completed | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 390686 | 373605 | 4338 | 768629 | 0.511832 |  |
| completed | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 1240120 | 1162636 | 6189 | 2408945 | 0.732171 |  |
| completed | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 481498 | 449398 | 5530 | 936426 | 0.495090 |  |
| completed | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 1104934 | 1029910 | 8042 | 2142886 | 0.710894 |  |
| completed | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 424958 | 403288 | 4437 | 832683 | 0.456698 |  |
| completed | fix-code-vulnerability | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 144283 | 129525 | 2941 | 276749 | 0.138274 |  |
| completed | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 8 | 128094 | 840 | 128942 | 0.079318 |  |
| completed | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 151805 | 132893 | 1075 | 285773 | 0.126905 |  |
| completed | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 178763 | 160715 | 311 | 339789 | 0.133496 |  |
| completed | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 155573 | 122402 | 202 | 278177 | 0.166887 |  |
| completed | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 192139 | 184736 | 152 | 377027 | 0.190627 |  |
| completed | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 127196 | 118322 | 237 | 245755 | 0.248832 |  |
| completed | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 84456 | 75816 | 3056 | 163328 | 0.100980 |  |
| completed | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 137682 | 128021 | 4244 | 269947 | 0.138285 |  |
| completed | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 194984 | 185867 | 2256 | 383107 | 0.123780 |  |
| completed | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 52633 | 46947 | 2500 | 102080 | 0.072874 |  |
| completed | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 211056 | 202088 | 2365 | 415509 | 0.129722 |  |
| completed | fix-git | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 30460 | 27036 | 2052 | 59548 | 0.051696 |  |
| completed | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 15 | 1233913 | 5392 | 1239320 | 1.146350 |  |
| completed | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 5438294 | 5360980 | 13508 | 10812782 |  |  |
| completed | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 1684186 | 1628407 | 1282 | 3313875 | 0.908985 |  |
| completed | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 3070358 | 2903574 | 3001 | 5976933 | 1.468496 |  |
| completed | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 1327802 | 1191590 | 665 | 2520057 | 1.875116 |  |
| completed | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 755957 | 576082 | 396 | 1332435 | 2.010518 |  |
| completed | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 658361 | 507083 | 23937 | 1189381 | 1.265992 |  |
| completed | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 1069267 | 993071 | 27528 | 2089866 | 0.996561 |  |
| completed | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 1076082 | 929658 | 26159 | 2031899 | 1.220014 |  |
| completed | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 757430 | 686950 | 22873 | 1467253 | 0.813466 |  |
| completed | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 616923 | 502179 | 13899 | 1133001 | 0.789348 |  |
| completed | fix-ocaml-gc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 722527 | 658370 | 20252 | 1401149 | 0.741340 |  |
| completed | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 4 | 47080 | 637 | 47721 |  |  |
| completed | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 27163 | 13458 | 332 | 40953 |  |  |
| completed | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 3731372 | 3538138 | 39569 | 7309079 |  |  |
| completed | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 3297066 | 3126433 | 27200 | 6450699 |  |  |
| completed | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 360238 | 309509 | 80 | 669827 | 2.211108 |  |
| completed | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 380705 | 345543 | 288 | 726536 | 0.697014 |  |
| completed | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 766941 | 704032 | 37700 | 1508673 |  |  |
| completed | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 859170 | 772325 | 54093 | 1685588 |  |  |
| completed | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 497031 | 469146 | 15662 | 981839 | 0.480228 |  |
| completed | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 385509 | 350898 | 14668 | 751075 | 0.454742 |  |
| completed | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 51728 | 46271 | 626 | 98625 |  |  |
| completed | gcode-to-text | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 878779 | 800474 | 43511 | 1722764 | 1.184900 |  |
| completed | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 7 | 101172 | 877 | 102056 | 0.104254 |  |
| completed | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 88639 | 73266 | 729 | 162634 | 0.090558 |  |
| completed | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 157013 | 140373 | 380 | 297766 | 0.125204 |  |
| completed | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 298225 | 251480 | 664 | 550369 | 0.285069 |  |
| completed | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 249635 | 246114 | 460 | 496209 | 0.200497 |  |
| completed | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 63313 | 55947 | 274 | 119534 | 0.126130 |  |
| completed | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 82996 | 76266 | 950 | 160212 | 0.062363 |  |
| completed | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 48461 | 45796 | 1483 | 95740 | 0.045971 |  |
| completed | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 134862 | 127839 | 1221 | 263922 | 0.082996 |  |
| completed | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 30139 | 27215 | 1600 | 58954 | 0.043121 |  |
| completed | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 146880 | 139433 | 1281 | 287594 | 0.088889 |  |
| completed | git-leak-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 28607 | 25129 | 2061 | 55797 | 0.051462 |  |
| completed | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 26 | 579408 | 3962 | 583396 | 0.323617 |  |
| completed | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 1363823 | 1334092 | 8772 | 2706687 | 0.643250 |  |
| completed | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 833270 | 820827 | 2267 | 1656364 | 0.387784 |  |
| completed | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 508992 | 418864 | 3104 | 930960 | 0.623961 |  |
| completed | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 729645 | 700508 | 1521 | 1431674 | 0.751293 |  |
| completed | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 1488735 | 1453241 | 2510 | 2944486 | 1.460723 |  |
| completed | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 600611 | 583410 | 6760 | 1190781 | 0.368865 |  |
| completed | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 309782 | 274554 | 6175 | 590511 | 0.307043 |  |
| completed | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 939135 | 865967 | 7456 | 1812558 | 0.645911 |  |
| completed | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 429220 | 397714 | 8680 | 835614 | 0.367170 |  |
| completed | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 1310460 | 1285885 | 10180 | 2606525 | 0.630584 |  |
| completed | git-multibranch | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 394086 | 373799 | 9276 | 777161 | 0.327330 |  |
| completed | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 54 | 2152364 | 46039 | 2198457 |  |  |
| completed | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 4986534 | 4906593 | 49711 | 9942838 |  |  |
| completed | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 2522519 | 2427301 | 2623 | 4952443 |  |  |
| completed | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 1131693 | 1026381 | 16433 | 2174507 | 0.908900 |  |
| completed | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 19372 | 18407 | 8 | 37787 |  |  |
| completed | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 4971 | 4427 | 6 | 9404 |  |  |
| completed | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 15727 | 10676 | 32000 | 58403 |  |  |
| completed | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 4857 | 0 | 32000 | 36857 |  |  |
| completed | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 0 | 0 | 0 | 0 |  |  |
| completed | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 1644 | 0 | 32000 | 33644 |  |  |
| completed | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 17196 | 11913 | 32000 | 61109 |  |  |
| completed | gpt2-codegolf | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 1621 | 0 | 32000 | 33621 |  |  |
| completed | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 8 | 116827 | 1881 | 118716 | 0.082028 |  |
| completed | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 86995 | 81408 | 1479 | 169882 | 0.067553 |  |
| completed | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 141900 | 138496 | 307 | 280703 | 0.086424 |  |
| completed | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 350047 | 291034 | 2149 | 643230 |  |  |
| completed | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 307557 | 275090 | 277 | 582924 | 0.592236 |  |
| completed | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 246689 | 225360 | 646 | 472695 | 0.573143 |  |
| completed | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 126321 | 116581 | 4420 | 247322 | 0.137793 |  |
| completed | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 344466 | 320097 | 15068 | 679631 | 0.413415 |  |
| completed | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 111427 | 100752 | 5176 | 217355 | 0.174042 |  |
| completed | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 166336 | 145015 | 13204 | 324555 | 0.321505 |  |
| completed | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 128626 | 115681 | 7300 | 251607 | 0.217612 |  |
| completed | headless-terminal | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 89904 | 72568 | 12520 | 174992 | 0.274572 |  |
| completed | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 14 | 225728 | 2218 | 227960 | 0.166605 |  |
| completed | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 254598 | 236888 | 3008 | 494494 | 0.182586 |  |
| completed | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 364783 | 344638 | 1033 | 710454 | 0.235709 |  |
| completed | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 1437882 | 1378569 | 2814 | 2819265 | 0.823709 |  |
| completed | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 869725 | 837432 | 1182 | 1708339 | 0.912926 |  |
| completed | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 72538 | 63252 | 186 | 135976 | 0.174037 |  |
| completed | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 275642 | 265457 | 3356 | 544455 | 0.168159 |  |
| completed | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 98347 | 92415 | 3521 | 194283 | 0.102774 |  |
| completed | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 117723 | 110831 | 1570 | 230124 | 0.082638 |  |
| completed | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 24509 | 21097 | 2464 | 48070 | 0.056077 |  |
| completed | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 165925 | 158394 | 1804 | 326123 | 0.102812 |  |
| completed | hf-model-inference | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 22193 | 18737 | 2527 | 43457 | 0.056480 |  |
| completed | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 43 | 999256 | 7664 | 1006963 | 0.475600 |  |
| completed | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 658960 | 645131 | 6591 | 1310682 | 0.344235 |  |
| completed | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 1238738 | 1220880 | 2402 | 2462020 | 0.560931 |  |
| completed | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 10122217 | 9999390 | 14624 | 20136231 | 4.586776 |  |
| completed | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 963786 | 949333 | 1313 | 1914432 | 0.839944 |  |
| completed | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 4043931 | 3964281 | 3842 | 8012054 | 4.073371 |  |
| completed | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 584290 | 567655 | 6430 | 1158375 | 0.329107 |  |
| completed | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 440817 | 414431 | 10446 | 865694 | 0.379876 |  |
| completed | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 6678344 | 6557600 | 63050 | 13298994 | 3.365733 |  |
| completed | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 2852124 | 2682380 | 43990 | 5578494 | 1.749200 |  |
| completed | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 2951126 | 2889171 | 24680 | 5864977 | 1.469180 |  |
| completed | install-windows-3.11 | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 1473551 | 1426746 | 29955 | 2930252 | 1.052016 |  |
| completed | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 9 | 131640 | 1407 | 133056 | 0.120174 |  |
| completed | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 251034 | 233741 | 2766 | 487541 | 0.176448 |  |
| completed | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 283543 | 265112 | 1057 | 549712 | 0.197386 |  |
| completed | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 415860 | 385033 | 2091 | 802984 | 0.278460 |  |
| completed | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 503334 | 477911 | 1142 | 982387 | 0.435683 |  |
| completed | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 76212 | 72398 | 285 | 148895 | 0.132264 |  |
| completed | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 150956 | 144124 | 1496 | 296576 | 0.091290 |  |
| completed | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 236676 | 223872 | 4086 | 464634 | 0.176448 |  |
| completed | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 159411 | 151344 | 1884 | 312639 | 0.103907 |  |
| completed | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 38601 | 34743 | 2336 | 75680 | 0.059922 |  |
| completed | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 192575 | 184163 | 1931 | 378669 | 0.115751 |  |
| completed | kv-store-grpc | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 41199 | 36303 | 2327 | 79829 | 0.064147 |  |
| completed | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 11 | 174310 | 1510 | 175831 | 0.138339 |  |
| completed | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 246373 | 228370 | 2583 | 477326 |  |  |
| completed | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 165732 | 147558 | 66 | 313356 | 0.147482 |  |
| completed | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 421958 | 377766 | 1867 | 801591 | 0.318798 |  |
| completed | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 316355 | 279211 | 137 | 595703 | 0.804204 |  |
| completed | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 164264 | 145898 | 153 | 310315 | 0.608361 |  |
| completed | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 200652 | 177126 | 17766 | 395544 | 0.407844 |  |
| completed | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 214610 | 192350 | 16366 | 423326 | 0.386660 |  |
| completed | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 177177 | 158183 | 13271 | 348631 | 0.317741 |  |
| completed | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 1027829 | 976995 | 46351 | 2051175 | 1.178872 |  |
| completed | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 664562 | 626068 | 31624 | 1322254 | 0.806495 |  |
| completed | large-scale-text-editing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 179113 | 160763 | 14814 | 354690 | 0.339241 |  |
| completed | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 27 | 639267 | 7667 | 646961 | 0.411808 |  |
| completed | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 842818 | 805452 | 15971 | 1664241 | 0.621298 |  |
| completed | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 511620 | 482315 | 855 | 994790 | 0.407673 |  |
| completed | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 2841371 | 2744709 | 32006 | 5618086 | 1.891704 |  |
| completed | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 40428 | 19413 | 16 | 59857 |  |  |
| completed | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 790271 | 729413 | 755 | 1520439 |  |  |
| completed | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 470398 | 428377 | 59109 | 957884 |  |  |
| completed | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 102929 | 60848 | 55691 | 219468 |  |  |
| completed | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 32833 | 26410 | 32140 | 91383 |  |  |
| completed | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 63765 | 30617 | 57332 | 151714 |  |  |
| completed | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 201179 | 168990 | 50423 | 420592 | 0.927743 |  |
| completed | largest-eigenval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 264734 | 215623 | 54782 | 535139 |  |  |
| completed | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 43 | 2665666 | 55132 | 2720841 | 1.985074 |  |
| completed | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 4374272 | 4257752 | 73558 | 8705582 | 2.817598 |  |
| completed | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 1775542 | 1702508 | 1692 | 3479742 | 1.352335 |  |
| completed | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 2147726 | 2042499 | 21163 | 4211388 | 1.847923 |  |
| completed | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 720586 | 622060 | 342 | 1342988 |  |  |
| completed | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 973815 | 772575 | 525 | 1746915 |  |  |
| completed | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 755897 | 563589 | 89975 | 1409461 |  |  |
| completed | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 651633 | 520379 | 112023 | 1284035 |  |  |
| completed | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 365664 | 266460 | 100235 | 732359 |  |  |
| completed | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 388572 | 227157 | 102415 | 718144 |  |  |
| completed | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 535810 | 457968 | 82809 | 1076587 |  |  |
| completed | llm-inference-batching-scheduler | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 403706 | 254210 | 98074 | 755990 |  |  |
| completed | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 4 | 55871 | 900 | 56775 | 0.097034 |  |
| completed | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 207412 | 186302 | 3279 | 396993 | 0.184229 |  |
| completed | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 66181 | 48414 | 179 | 114774 | 0.094452 |  |
| completed | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 124825 | 78426 | 229 | 203480 | 0.196300 |  |
| completed | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 85766 | 63021 | 109 | 148896 | 0.213468 |  |
| completed | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 52792 | 46115 | 144 | 99051 | 0.142512 |  |
| completed | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 90876 | 82156 | 1441 | 174473 | 0.078957 |  |
| completed | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 137081 | 99218 | 1628 | 237927 | 0.196167 |  |
| completed | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 129151 | 119588 | 2424 | 251163 | 0.108092 |  |
| completed | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 31206 | 24841 | 2808 | 58855 | 0.073436 |  |
| completed | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 96914 | 88052 | 1594 | 186560 | 0.083493 |  |
| completed | log-summary-date-ranges | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 23639 | 17054 | 2226 | 42919 | 0.063195 |  |
| completed | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 56 | 2499392 | 9069 | 2508517 | 1.092627 |  |
| completed | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 9537964 | 9457446 | 29809 | 19025219 | 3.586171 |  |
| completed | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 2443945 | 2394627 | 2724 | 4841296 | 1.059505 |  |
| completed | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 2219390 | 2063474 | 5079 | 4287943 | 1.370109 |  |
| completed | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 2093296 | 2049424 | 1465 | 4144185 | 1.986162 |  |
| completed | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 1418501 | 1374521 | 1763 | 2794785 | 1.530018 |  |
| completed | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 4682291 | 4600327 | 38469 | 9321087 | 2.325576 |  |
| completed | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 1132355 | 1095126 | 12397 | 2239878 | 0.652907 |  |
| completed | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 3304831 | 3246650 | 27486 | 6578967 | 1.713094 |  |
| completed | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 845111 | 805903 | 22348 | 1673362 | 0.721645 |  |
| completed | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 1907813 | 1866263 | 15027 | 3789103 | 0.940680 |  |
| completed | mailman | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 1559565 | 1518775 | 16763 | 3095103 | 0.859992 |  |
| completed | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 87 | 10151464 | 71547 | 10223098 |  |  |
| completed | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 6165519 | 6071037 | 54219 | 12290775 |  |  |
| completed | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 9731995 | 9560233 | 5057 | 19297285 | 5.006167 |  |
| completed | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 8553226 | 8009057 | 51827 | 16614110 |  |  |
| completed | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 1574848 | 1326510 | 275 | 2901633 |  |  |
| completed | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 3219445 | 2904272 | 1136 | 6124853 |  |  |
| completed | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 436259 | 292672 | 118663 | 847594 |  |  |
| completed | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 3350778 | 3185702 | 106139 | 6642619 |  |  |
| completed | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 1014415 | 751471 | 94725 | 1860611 |  |  |
| completed | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 3728739 | 3399921 | 108197 | 7236857 |  |  |
| completed | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 1761505 | 1618431 | 83242 | 3463178 |  |  |
| completed | make-mips-interpreter | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 1251030 | 985553 | 106995 | 2343578 |  |  |
| completed | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 27 | 523784 | 3478 | 527289 |  |  |
| completed | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 17478342 | 17375730 | 38319 | 34892391 | 6.172066 |  |
| completed | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 845824 | 779430 | 1733 | 1626987 | 0.576497 |  |
| completed | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 688078 | 628854 | 1440 | 1318372 | 0.512225 |  |
| completed | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 1838383 | 1708214 | 1237 | 3547834 | 1.958108 |  |
| completed | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 260879 | 229318 | 1209 | 491406 |  |  |
| completed | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 417632 | 382970 | 3248 | 803850 |  |  |
| completed | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 224761 | 202331 | 4102 | 431194 |  |  |
| completed | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 1559299 | 1505017 | 10279 | 3074595 | 0.809212 |  |
| completed | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 820652 | 760365 | 12647 | 1593664 |  |  |
| completed | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 2213235 | 2154742 | 13412 | 4381389 |  |  |
| completed | mcmc-sampling-stan | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 215410 | 201702 | 4352 | 421464 |  |  |
| completed | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 30 | 829329 | 6804 | 836163 | 0.477222 |  |
| completed | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 835507 | 804449 | 5914 | 1645870 | 0.446487 |  |
| completed | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 444718 | 418926 | 973 | 864617 | 0.297906 |  |
| completed | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 770927 | 688908 | 7669 | 1467504 | 0.781702 |  |
| completed | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 614250 | 581353 | 1081 | 1196684 | 0.763294 |  |
| completed | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 198336 | 181577 | 599 | 380512 | 0.402130 |  |
| completed | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 307293 | 290887 | 7065 | 605245 | 0.254753 |  |
| completed | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 245520 | 231948 | 8732 | 486200 | 0.251446 |  |
| completed | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 331705 | 313273 | 9053 | 654031 | 0.298886 |  |
| completed | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 153846 | 138909 | 9805 | 302560 | 0.244750 |  |
| completed | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 364963 | 345139 | 9919 | 720021 | 0.326394 |  |
| completed | merge-diff-arc-agi-task | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 154823 | 142791 | 6448 | 304062 | 0.183545 |  |
| completed | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 9 | 172507 | 6404 | 178920 | 0.242373 |  |
| completed | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 1642589 | 1581705 | 31127 | 3255421 | 1.169697 |  |
| completed | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 1161099 | 1091338 | 682 | 2253119 | 0.920364 |  |
| completed | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 237252 | 158252 | 2876 | 398380 | 0.445825 |  |
| completed | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 342165 | 284715 | 283 | 627163 |  |  |
| completed | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 572802 | 507894 | 417 | 1081113 | 1.745356 |  |
| completed | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 1240589 | 1172856 | 53369 | 2466814 |  |  |
| completed | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 217847 | 182773 | 49135 | 449755 |  |  |
| completed | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 470483 | 425362 | 38130 | 933975 | 0.868753 |  |
| completed | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 464131 | 408319 | 52302 | 924752 |  |  |
| completed | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 202335 | 152696 | 50194 | 405225 |  |  |
| completed | model-extraction-relu-logits | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 239240 | 196150 | 37994 | 473384 |  |  |
| completed | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 5 | 77257 | 1021 | 78283 | 0.110850 |  |
| completed | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 50286 | 31724 | 759 | 82769 | 0.090507 |  |
| completed | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 49496 | 31735 | 113 | 81344 | 0.091931 |  |
| completed | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 105108 | 58757 | 169 | 164034 | 0.185998 |  |
| completed | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 158608 | 153128 | 288 | 312024 | 0.169654 |  |
| completed | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 171949 | 157310 | 351 | 329610 | 0.346922 |  |
| completed | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 52435 | 43874 | 1058 | 97367 | 0.060655 |  |
| completed | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 101679 | 91321 | 5159 | 198159 | 0.143492 |  |
| completed | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 70886 | 62703 | 1065 | 134654 | 0.065295 |  |
| completed | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 55728 | 44324 | 5744 | 105796 | 0.142076 |  |
| completed | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 76977 | 68488 | 1085 | 146550 | 0.068478 |  |
| completed | modernize-scientific-stack | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 54218 | 44017 | 5037 | 103272 | 0.126774 |  |
| completed | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 3 | 31102 | 200 | 31305 | 0.066677 |  |
| completed | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 627461 | 596846 | 3862 | 1228169 |  |  |
| completed | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 327390 | 289190 | 781 | 617361 |  |  |
| completed | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 3036746 | 2797961 | 6373 | 5841080 |  |  |
| completed | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 308577 | 268704 | 317 | 577598 |  |  |
| completed | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 10495364 | 10187603 | 5602 | 20688569 | 8.399906 |  |
| completed | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 9263280 | 9133966 | 52962 | 18450208 | 5.503129 |  |
| completed | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 5134341 | 4948923 | 48094 | 10131358 | 2.514052 |  |
| completed | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 5648342 | 5544099 | 51095 | 11243536 | 3.699881 |  |
| completed | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 6634875 | 6483493 | 57804 | 13176172 | 3.379713 |  |
| completed | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 5200146 | 5104716 | 38468 | 10343330 | 4.481064 |  |
| completed | mteb-leaderboard | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 9406344 | 9119950 | 73017 | 18599311 | 4.367676 |  |
| completed | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 5 | 63521 | 602 | 64128 | 0.085199 |  |
| completed | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 164223 | 148115 | 2105 | 314443 | 0.136405 |  |
| completed | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 90332 | 74634 | 308 | 165274 | 0.096297 |  |
| completed | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 153996 | 109311 | 1095 | 264402 | 0.198209 |  |
| completed | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 80136 | 59515 | 133 | 139784 | 0.189857 |  |
| completed | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 31333 | 28415 | 134 | 59882 | 0.069768 |  |
| completed | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 81857 | 75500 | 956 | 158313 | 0.060824 |  |
| completed | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 23399 | 21148 | 1089 | 45636 | 0.031117 |  |
| completed | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 82074 | 75788 | 870 | 158732 | 0.059354 |  |
| completed | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 23975 | 18740 | 2617 | 45332 | 0.064502 |  |
| completed | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 70643 | 64505 | 753 | 135901 | 0.053660 |  |
| completed | mteb-retrieve | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 50686 | 45463 | 2679 | 98828 | 0.073400 |  |
| completed | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 9 | 139300 | 2243 | 141552 | 0.142137 |  |
| completed | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 232132 | 210940 | 5549 | 448621 | 0.225976 |  |
| completed | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 172846 | 152897 | 430 | 326173 | 0.176566 |  |
| completed | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 251298 | 203001 | 3086 | 457385 | 0.289345 |  |
| completed | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 223471 | 198460 | 439 | 422370 | 0.360073 |  |
| completed | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 79052 | 64884 | 216 | 144152 | 0.332918 |  |
| completed | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 110204 | 100283 | 3639 | 214126 | 0.121868 |  |
| completed | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 61828 | 51272 | 4660 | 117760 | 0.124860 |  |
| completed | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 93206 | 83363 | 3218 | 179787 | 0.135913 |  |
| completed | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 28660 | 20933 | 5083 | 54676 | 0.111496 |  |
| completed | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 117765 | 107929 | 3342 | 229036 | 0.119388 |  |
| completed | multi-source-data-merger | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 45830 | 32936 | 10157 | 88923 | 0.210583 |  |
| completed | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 12 | 198179 | 1665 | 199856 | 0.151743 |  |
| completed | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 244678 | 226375 | 2487 | 473540 | 0.173842 |  |
| completed | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 353896 | 333996 | 1094 | 688986 | 0.221263 |  |
| completed | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 522953 | 472867 | 3685 | 999505 | 0.393921 |  |
| completed | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 459711 | 434072 | 1039 | 894822 | 0.496722 |  |
| completed | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 113563 | 102209 | 334 | 216106 | 0.228822 |  |
| completed | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 195760 | 187367 | 1919 | 385046 | 0.116460 |  |
| completed | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 93180 | 82444 | 2720 | 178344 | 0.105570 |  |
| completed | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 175570 | 167486 | 1586 | 344642 | 0.104343 |  |
| completed | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 51979 | 45931 | 3189 | 101099 | 0.084285 |  |
| completed | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 213362 | 204481 | 1884 | 419727 | 0.122899 |  |
| completed | nginx-request-logging | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 41251 | 36113 | 2966 | 80330 | 0.074583 |  |
| completed | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 13 | 200280 | 1572 | 201865 | 0.145185 |  |
| completed | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 236612 | 231793 | 3138 | 471543 | 0.134667 |  |
| completed | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 307786 | 301828 | 1045 | 610659 | 0.174392 |  |
| completed | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 411028 | 405226 | 2065 | 818319 | 0.224283 |  |
| completed | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 371060 | 365211 | 997 | 737268 | 0.335633 |  |
| completed | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 79272 | 71181 | 96 | 150549 | 0.209582 |  |
| completed | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 132613 | 125759 | 1301 | 259673 | 0.082938 |  |
| completed | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 99766 | 92538 | 3519 | 195823 | 0.107640 |  |
| completed | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 189747 | 181523 | 2183 | 373453 | 0.118033 |  |
| completed | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 31537 | 27102 | 3185 | 61824 | 0.072529 |  |
| completed | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 163512 | 156214 | 1434 | 321160 | 0.095734 |  |
| completed | openssl-selfsigned-cert | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 31013 | 26741 | 3054 | 60808 | 0.069844 |  |
| completed | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 37 | 1373814 | 8396 | 1382247 | 0.684154 |  |
| completed | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 2372841 | 2326667 | 16159 | 4715667 | 1.113490 |  |
| completed | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 702746 | 681843 | 825 | 1385414 | 0.388398 |  |
| completed | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 1932222 | 1894194 | 2538 | 3828954 | 0.947469 |  |
| completed | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 1594070 | 1522338 | 1528 | 3117936 |  |  |
| completed | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 721795 | 671791 | 734 | 1394320 | 1.521852 |  |
| completed | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 745097 | 695963 | 26212 | 1467272 | 1.113434 |  |
| completed | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 493772 | 462388 | 21705 | 977865 | 0.581965 |  |
| completed | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 1456999 | 1412615 | 31773 | 2901387 | 1.066791 |  |
| completed | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 646830 | 591955 | 41892 | 1280677 |  |  |
| completed | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 1339833 | 1290450 | 37897 | 2668180 |  |  |
| completed | overfull-hbox | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 703552 | 648891 | 40784 | 1393227 |  |  |
| completed | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 30 | 653325 | 10065 | 663420 | 0.455113 |  |
| completed | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 5368757 | 5134006 | 42355 | 10545118 |  |  |
| completed | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 480693 | 451393 | 905 | 932991 | 0.345126 |  |
| completed | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 1463720 | 1396841 | 4339 | 2864900 | 1.022164 |  |
| completed | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 2465290 | 2408332 | 1461 | 4875083 | 2.695245 |  |
| completed | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 537076 | 499641 | 877 | 1037594 | 1.144754 |  |
| completed | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 1038028 | 974174 | 16529 | 2028731 | 0.766074 |  |
| completed | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 541993 | 505569 | 18926 | 1066488 | 0.570004 |  |
| completed | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 641286 | 604771 | 17065 | 1263122 | 0.573443 |  |
| completed | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 806202 | 760699 | 31637 | 1598538 | 0.873051 |  |
| completed | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 516790 | 492426 | 12497 | 1021713 | 0.425647 |  |
| completed | password-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 275437 | 235094 | 18926 | 529457 | 0.505599 |  |
| completed | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 145 | 12862398 | 103246 | 12965789 |  |  |
| completed | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 4871071 | 4593750 | 74673 | 9539494 |  |  |
| completed | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 6674749 | 6521488 | 7505 | 13203742 |  |  |
| completed | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 3575580 | 3304237 | 77886 | 6957703 |  |  |
| completed | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 954229 | 738667 | 578 | 1693474 |  |  |
| completed | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 909077 | 631759 | 602 | 1541438 |  |  |
| completed | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 428731 | 312038 | 77351 | 818120 |  |  |
| completed | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 2063154 | 1911487 | 104089 | 4078730 |  |  |
| completed | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 1013708 | 837504 | 95209 | 1946421 |  |  |
| completed | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 321279 | 192384 | 111601 | 625264 |  |  |
| completed | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 1874450 | 1741034 | 101783 | 3717267 |  |  |
| completed | path-tracing | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 684904 | 480870 | 112660 | 1278434 |  |  |
| completed | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 115 | 9290794 | 85585 | 9376494 | 5.419259 |  |
| completed | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 8994603 | 8767952 | 82109 | 17844664 | 5.376384 |  |
| completed | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 5966729 | 5523990 | 10226 | 11500945 |  |  |
| completed | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 6489646 | 6091349 | 34674 | 12615669 |  |  |
| completed | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 2300206 | 2080000 | 2292 | 4382498 |  |  |
| completed | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 1521092 | 1231993 | 1002 | 2754087 |  |  |
| completed | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 1873791 | 1751342 | 102809 | 3727942 |  |  |
| completed | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 1696410 | 1375927 | 92179 | 3164516 |  |  |
| completed | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 950408 | 743383 | 107837 | 1801628 |  |  |
| completed | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 1536398 | 1309739 | 84983 | 2931120 |  |  |
| completed | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 691964 | 599743 | 54185 | 1345892 |  |  |
| completed | path-tracing-reverse | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 1887346 | 1519561 | 106420 | 3513327 |  |  |
| completed | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 33 | 781184 | 13217 | 794434 | 0.548084 |  |
| completed | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 173888 | 155799 | 2864 | 332551 | 0.157524 |  |
| completed | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 381933 | 354877 | 446 | 737256 | 0.442020 |  |
| completed | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 102260 | 56598 | 106 | 158964 | 0.188448 |  |
| completed | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 121710 | 95712 | 137 | 217559 | 0.383117 |  |
| completed | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 108210 | 93909 | 237 | 202356 | 0.362645 |  |
| completed | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 123034 | 106560 | 11534 | 241128 | 0.266751 |  |
| completed | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 62755 | 50908 | 6746 | 120409 | 0.160883 |  |
| completed | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 116023 | 106215 | 4780 | 227018 | 0.140339 |  |
| completed | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 105206 | 82184 | 19650 | 207040 | 0.405732 |  |
| completed | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 148718 | 127308 | 16042 | 292068 | 0.359105 |  |
| completed | polyglot-c-py | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 72213 | 55664 | 47506 | 175383 |  |  |
| completed | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 88 | 3668979 | 41624 | 3710691 | 1.897621 |  |
| completed | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 1951325 | 1891015 | 37347 | 3879687 | 1.471685 |  |
| completed | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 1345092 | 1301346 | 3130 | 2649568 | 1.143133 |  |
| completed | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 485290 | 397815 | 23193 | 906298 | 0.801393 |  |
| completed | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 19390 | 0 | 8 | 19398 |  |  |
| completed | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 4989 | 0 | 6 | 4995 |  |  |
| completed | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 15745 | 10676 | 32000 | 58421 |  |  |
| completed | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 34626 | 0 | 52038 | 86664 |  |  |
| completed | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 15711 | 10676 | 32000 | 58387 |  |  |
| completed | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 1662 | 0 | 32000 | 33662 |  |  |
| completed | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 178219 | 148452 | 51211 | 377882 | 0.924320 |  |
| completed | polyglot-rust-c | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 52144 | 25319 | 54985 | 132448 |  |  |
| completed | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 6 | 127976 | 2477 | 130459 | 0.135648 |  |
| completed | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 722917 | 692359 | 7361 | 1422637 | 0.432693 |  |
| completed | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 253110 | 228162 | 528 | 481800 | 0.210669 |  |
| completed | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 372776 | 318570 | 2251 | 693597 | 0.338021 |  |
| completed | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 332326 | 301100 | 622 | 634048 | 0.523008 |  |
| completed | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 87029 | 75362 | 137 | 162528 | 0.276010 |  |
| completed | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 149745 | 135298 | 4987 | 290030 | 0.169565 |  |
| completed | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 92589 | 77788 | 10377 | 180754 | 0.234489 |  |
| completed | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 153851 | 138361 | 6233 | 298445 | 0.193085 |  |
| completed | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 60737 | 49125 | 5996 | 115858 | 0.148215 |  |
| completed | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 187662 | 164405 | 12045 | 364112 | 0.315974 |  |
| completed | portfolio-optimization | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 58661 | 46643 | 6591 | 111895 | 0.156970 |  |
| completed | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 5 | 63887 | 515 | 64407 | 0.083386 |  |
| completed | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 56437 | 41924 | 445 | 98806 | 0.073672 |  |
| completed | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 91255 | 75463 | 246 | 166964 | 0.095654 |  |
| completed | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 117304 | 72993 | 114 | 190411 | 0.181902 |  |
| completed | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 206880 | 182377 | 350 | 389607 | 0.364835 |  |
| completed | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 56454 | 47215 | 263 | 103932 | 0.179594 |  |
| completed | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 104643 | 96199 | 3316 | 204158 | 0.110259 |  |
| completed | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 39547 | 31918 | 2648 | 74113 | 0.077899 |  |
| completed | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 103018 | 95065 | 2913 | 200996 | 0.102033 |  |
| completed | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 26483 | 21553 | 4203 | 52239 | 0.087993 |  |
| completed | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 96975 | 87978 | 3705 | 188658 | 0.115703 |  |
| completed | prove-plus-comm | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 21009 | 17301 | 2784 | 41094 | 0.060850 |  |
| completed | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 18 | 301689 | 1767 | 303474 | 0.185776 |  |
| completed | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 272018 | 253694 | 2331 | 528043 | 0.179775 |  |
| completed | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 192664 | 174732 | 679 | 368075 |  |  |
| completed | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 384282 | 336622 | 1085 | 721989 | 0.308953 |  |
| completed | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 607993 | 596705 | 1353 | 1206051 | 0.502466 |  |
| completed | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 168062 | 160656 | 598 | 329316 | 0.233034 |  |
| completed | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 190724 | 182127 | 1647 | 374498 | 0.111573 |  |
| completed | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 177361 | 170285 | 3347 | 350993 | 0.127808 |  |
| completed | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 252681 | 243287 | 2116 | 498084 | 0.139942 |  |
| completed | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 77741 | 70844 | 2806 | 151391 | 0.089194 |  |
| completed | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 272618 | 263044 | 2072 | 537734 | 0.145884 |  |
| completed | pypi-server | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 58806 | 52215 | 2750 | 113771 | 0.081620 |  |
| completed | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 3 | 44561 | 416 | 44980 | 0.076794 |  |
| completed | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 354882 | 334407 | 3265 | 692554 |  |  |
| completed | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 487366 | 475750 | 1036 | 964152 | 0.296576 |  |
| completed | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 742599 | 714308 | 5003 | 1461910 | 0.456994 |  |
| completed | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 777620 | 758602 | 872 | 1537094 | 0.838134 |  |
| completed | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 257944 | 243272 | 509 | 501725 | 0.460311 |  |
| completed | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 274990 | 260844 | 6571 | 542405 | 0.229855 |  |
| completed | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 160874 | 146979 | 6149 | 314002 | 0.188421 |  |
| completed | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 524269 | 506608 | 9206 | 1040083 | 0.356283 |  |
| completed | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 50198 | 43346 | 4284 | 97828 | 0.102950 |  |
| completed | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 362989 | 349879 | 5863 | 718731 | 0.242058 |  |
| completed | pytorch-model-cli | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 124132 | 112974 | 7889 | 244995 | 0.194055 |  |
| completed | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 |  |  |  |  |  |  |
| completed | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 |  |  |  |  |  |  |
| completed | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 |  |  |  |  |  |  |
| completed | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 |  |  |  |  |  |  |
| completed | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 |  |  |  |  |  |  |
| completed | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 |  |  |  |  |  |  |
| completed | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 |  |  |  |  |  |  |
| completed | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 |  |  |  |  |  |  |
| completed | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 |  |  |  |  |  |  |
| completed | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 |  |  |  |  |  |  |
| completed | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 |  |  |  |  |  |  |
| completed | pytorch-model-recovery | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 |  |  |  |  |  |  |
| completed | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 |  |  |  |  |  |  |
| completed | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 |  |  |  |  |  |  |
| completed | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 |  |  |  |  |  |  |
| completed | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-alpine-ssh | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 |  |  |  |  |  |  |
| completed | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 |  |  |  |  |  |  |
| completed | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 |  |  |  |  |  |  |
| completed | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 |  |  |  |  |  |  |
| completed | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 |  |  |  |  |  |  |
| completed | qemu-startup | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 |  |  |  |  |  |  |
| completed | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 12 | 223197 | 2498 | 225707 | 0.181417 |  |
| completed | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 599405 | 572502 | 5313 | 1177220 | 0.352309 |  |
| completed | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 195688 | 175041 | 289 | 371018 | 0.181095 |  |
| completed | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 366140 | 308804 | 1855 | 676799 | 0.420194 |  |
| completed | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 366925 | 324258 | 233 | 691416 |  |  |
| completed | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 105505 | 96404 | 223 | 202132 |  |  |
| completed | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 320621 | 305884 | 7124 | 633629 | 0.289459 |  |
| completed | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 230016 | 213244 | 9015 | 452275 |  |  |
| completed | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 186656 | 174664 | 4935 | 366255 |  |  |
| completed | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 78400 | 68949 | 5338 | 152687 |  |  |
| completed | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 397363 | 363455 | 7847 | 768665 | 0.302881 |  |
| completed | query-optimize | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 126696 | 114098 | 8138 | 248932 |  |  |
| completed | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 52 | 2848841 | 56182 | 2905075 | 2.124414 |  |
| completed | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 768653 | 723789 | 23466 | 1515908 | 0.737345 |  |
| completed | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 1485807 | 1418540 | 2647 | 2906994 | 1.229750 |  |
| completed | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 2006704 | 1894158 | 34564 | 3935426 |  |  |
| completed | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 631392 | 563778 | 435 | 1195605 |  |  |
| completed | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 769919 | 707651 | 995 | 1478565 |  |  |
| completed | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 460144 | 424550 | 22208 | 906902 | 0.593947 |  |
| completed | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 474628 | 430489 | 31664 | 936781 | 0.769609 |  |
| completed | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 492572 | 454267 | 25393 | 972232 | 0.660805 |  |
| completed | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 718909 | 646534 | 51918 | 1417361 | 1.244117 |  |
| completed | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 1088762 | 1017198 | 52116 | 2158076 |  |  |
| completed | raman-fitting | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 508673 | 443797 | 40441 | 992911 | 0.983022 |  |
| completed | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 179 | 17956806 | 153215 | 18110200 | 9.376270 |  |
| completed | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 19961180 | 19665506 | 206034 | 39832720 |  |  |
| completed | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 7093055 | 6862673 | 5623 | 13961351 | 5.001812 |  |
| completed | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 5006058 | 4751791 | 58567 | 9816416 | 4.459633 |  |
| completed | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 88494 | 39616 | 1597 | 129707 |  |  |
| completed | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 117831 | 43958 | 110 | 161899 | 4.071696 |  |
| completed | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 141877 | 69583 | 169392 | 380852 | 2.832846 |  |
| completed | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 39621 | 5333 | 160106 | 205060 | 2.531759 |  |
| completed | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 104817 | 69549 | 160151 | 334517 | 2.555373 |  |
| completed | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 51923 | 3220 | 168276 | 223419 | 2.707731 |  |
| completed | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 70782 | 47652 | 128000 | 246434 | 2.021025 |  |
| completed | regex-chess | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 19345 | 4251 | 160156 | 183752 | 2.460207 |  |
| completed | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 6 | 90319 | 2829 | 93154 | 0.139670 |  |
| completed | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 2143764 | 2098117 | 29971 | 4271852 | 1.250128 |  |
| completed | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 96995 | 79181 | 55 | 176231 | 0.126132 |  |
| completed | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 104214 | 46271 | 2988 | 153473 | 0.328779 |  |
| completed | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 55600 | 37900 | 9 | 93509 | 0.557546 |  |
| completed | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 87071 | 63691 | 69 | 150831 | 0.743467 |  |
| completed | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 90320 | 57807 | 21881 | 170008 | 0.467478 |  |
| completed | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 186322 | 149397 | 25985 | 361704 | 0.573057 |  |
| completed | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 82506 | 59134 | 17941 | 159581 | 0.374497 |  |
| completed | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 102015 | 75236 | 23874 | 201125 | 0.481098 |  |
| completed | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 93015 | 66446 | 20914 | 180375 | 0.433275 |  |
| completed | regex-log | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 178691 | 140309 | 33899 | 352899 | 0.694505 |  |
| completed | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 1.0 | 60 | 5716388 | 35326 | 5751774 |  |  |
| completed | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 1.0 | 2087629 | 2001153 | 9042 | 4097824 | 1.059626 |  |
| completed | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 840384 | 765992 | 5574 | 1611950 | 0.702401 |  |
| completed | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 916072 | 813423 | 6520 | 1736015 | 0.669452 |  |
| completed | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 1.0 | 1155440 | 1076398 | 935 | 2232773 | 2.039040 |  |
| completed | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 1.0 | 1371354 | 1326102 | 1346 | 2698802 | 1.752629 |  |
| completed | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 1.0 | 1036959 | 993354 | 29280 | 2059593 | 0.975540 |  |
| completed | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 1.0 | 1226906 | 1162385 | 41871 | 2431162 | 1.218713 |  |
| completed | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 1.0 | 405004 | 375894 | 21577 | 802475 | 0.593284 |  |
| completed | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 1.0 | 582278 | 547594 | 23362 | 1153234 | 0.643261 |  |
| completed | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 1.0 | 763077 | 724924 | 25622 | 1513623 | 0.854796 |  |
| completed | reshard-c4-data | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 1.0 | 970027 | 919426 | 33066 | 1922519 | 0.961523 |  |
| completed | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 5 | 79764 | 2363 | 82132 | 0.188944 |  |
| completed | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 351202 | 314793 | 5001 | 670996 | 0.392515 |  |
| completed | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 232113 | 189677 | 6206 | 427996 | 0.367720 |  |
| completed | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 298699 | 225031 | 2455 | 526185 | 0.356950 |  |
| completed | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 1886471 | 1814443 | 1284 | 3702198 | 2.292366 |  |
| completed | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 369340 | 342277 | 948 | 712565 | 0.737772 |  |
| completed | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 586720 | 558668 | 11189 | 1156577 | 0.440613 |  |
| completed | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 1007737 | 941949 | 36107 | 1985793 | 1.070285 |  |
| completed | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 155335 | 136271 | 9258 | 300864 | 0.250650 |  |
| completed | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 292342 | 257095 | 17089 | 566526 | 0.465623 |  |
| completed | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 604170 | 572867 | 14663 | 1191700 | 0.509174 |  |
| completed | sam-cell-seg | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 991933 | 930421 | 37635 | 1959989 | 1.074294 |  |
| completed | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 8 | 279770 | 2435 | 282213 | 0.708977 |  |
| completed | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 1411500 | 1322054 | 5959 | 2739513 | 0.941313 |  |
| completed | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 0.0 | 1160591 | 1054645 | 340 | 2215576 | 0.781765 |  |
| completed | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 0.0 | 871561 | 765438 | 2422 | 1639421 | 0.565776 |  |
| completed | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular | 0.0 | 646919 | 609225 | 271 | 1256415 | 0.754248 |  |
| completed | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple | 0.0 | 668210 | 587999 | 453 | 1256662 | 1.098908 |  |
| completed | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular | 0.0 | 151243 | 131545 | 2873 | 285661 | 0.259065 |  |
| completed | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple | 0.0 | 644909 | 580795 | 6989 | 1232693 | 0.519408 |  |
| completed | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular | 0.0 | 288604 | 267240 | 3805 | 559649 | 0.352218 |  |
| completed | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple | 0.0 | 818563 | 748534 | 7300 | 1574397 | 0.596549 |  |
| completed | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular | 0.0 | 167235 | 150741 | 2616 | 320592 | 0.208818 |  |
| completed | sanitize-git-repo | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | simple | 0.0 | 479756 | 423865 | 6555 | 910176 | 0.433821 |  |
| completed | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 0.2.66 | regular | 0.0 | 6 | 159978 | 1011 | 160995 | 0.200849 |  |
| completed | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 1.0.0 | regular | 0.0 | 6694213 | 6514802 | 95571 | 13304586 |  |  |
| completed | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.0.0 | regular | 1.0 | 3855553 | 3792484 | 3530 | 7651567 |  |  |
| completed | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.0 | regular | 1.0 | 4842717 | 4684901 | 26497 | 9554115 | 2.639484 |  |
| running | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | regular |  |  |  |  |  |  |  |
| running | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.48 | simple |  |  |  |  |  |  |  |
| running | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | regular |  |  |  |  |  |  |  |
| running | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.113 | simple |  |  |  |  |  |  |  |
| running | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | regular |  |  |  |  |  |  |  |
| running | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.116 | simple |  |  |  |  |  |  |  |
| running | schemelike-metacircular-eval | versioned-claude-code | anthropic/claude-sonnet-4-6 | 2.1.145 | regular |  |  |  |  |  |  |  |
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
