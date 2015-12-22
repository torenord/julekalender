S = """TAACGAGTCTGCCACTAGATAGCCCGCGCTATTAATGGGATGTTCTAGGTCTTCACCTCGACCTATACAAGACGAGAAT
       TCTGGTTCAGCCGGTCCGGGGTCGGGAGTTTGGCTTCATAACACAATTGCAGGCGTCAGAGGCCATACCTTAAACCCAT
       CATACGACCGGTACGAAAATCCATGTCACAGACTAATGATCCCTGCTAAGAGATCGTAGCAACCGTTCTGGATCCAAGC
       AGCTAATAAGTTAGCAAGCTGGTGTGTTTTTGATATTTGCAGTGGCAAACTGTTGCCTGGGTCGGTCCGATGGTCCTCA
       TCGGACGCTGATGACGGACTTTGCACGGTCGCAAGTCGCTGATAGAAGGTGACTCTCGTGCACGATTTAGACCGGCAGT
       GCTGCGTGAAGGGGGCTCCCTTATCTGATATGCGCAGACTATTTCGGCGTGGAATGCACATGTTCCCCGACCACTTCAA
       CCCTCATGTTGAGGACTTCCTGCCATAACAACAGGGTAACTTAACTCAGGATGTCTTAAAAAAATAGGCTTCTCATGTG
       CTCACATTTGGGACCGTATGTGCTAAACGGTGTACTATACGCGGTGGAATTTGGAATGGCAAACTTAACAGCAGGTCTA
       ACCGTAGAAGACGTTACGAGTAAGTGTCAAGTCAGCATTGGCGGATCACGGCGTCGCTATGCCGTCAAGCTCTTTTGCG
       GATATGATCTAAATCAGATTACGAGCGACGCCTGTTTCTAAAATGACCAATGGTACGCAACACGCTGGTAGGATCTGAG
       CGAGCAAAGCATAAATAGACCCATCGTGTCGCCTGTAAATTGCAAGAGTACCAAGAACCCCGCAATTACGTTGGGTTCG
       CTATAGTTGAAAGTTACCGATAAACTACCTTTCGCGACCCGTTTTATAACATAACTAGCATTATTACTCAAGGTGCTCT
       GATTCCCAGAATACCCAAGAACTAGCGCGTTTTTATTTCTTTGGGGAGGTCTTGTCATGATGTTCATACTTGTCGCCTA
       GGTTTGCCGACTTGTCCTTCTCTTACACTATTCCGAAATCGCAGTTGCACCACGATCGATGAGCATGGTAGTTACTTAA
       ATATTCAAGAGTCCTGGTCCTCGAAATGGCATATGCTTGCAGGTGCCCCCGATCAGATAGAAGACCGCGGCCGAGGAGG
       TAGTCCGGTACTGTGCGTTTGGTGCCTTTGACTCTTTACGCACTACTGGACCGGCCTTCGAGGTCTAAGGCTACGTCCT
       TTAACGCTTTTACTATACAATAGAAGGTGTTCTACACACTGCGTGTCGCTGGATTGGCCTTCGACACGCCTTAGCGGCA
       TGTATCAAGCTATCAGGGAGCCCATTGTGGGCGGTTACTCGTCGTTTGCACAACATCAGACCATTCACTATTAAGCTCA
       TCCCCGAAGAAGGCACCCTACCGTTGTAAGTGCGACTTTGGAACCTCTCGGTAATGCCGGTTGCGGCACTTTCAACGTA
       CATTCCGACCTAGTGCAGAAGAATGGATAGCGAGCTGTTTTTCGAGCTCTACCTAATCGGCTCGAATCTACTCGACGTG
       TCGAGCGTCCTGTCGCATGGCTCGAAGCGGTATCGAGTCAGTCCCCCAGGGGCGCCGACACGTAGTGAGGTGAAAACAT
       CGACATGTGCTTTTGATGTATATGGCTGAGCTTCAATGCGTGGCTAAAGTGGTCAATCCACTCAGGGCATGGATACTCG
       GCTCAACATAGTAAATTGTCTCCGCGTCCGATAGGCGGGGGTCAATCCGCCGCACTGGTGGGTCACCCGTGATGCTAGG
       TCTATAGCAGGGCCCCGACCGTAAACTTCAAGCTTTCCCGGTTGCTGTTGTTTTTTGAGCACAGGGAAACGAGCAGTAT
       TGAATCTGAAGGGGGATAGGCGTTTAATTATTCAGAAGTAGTGCGAAGGGCTCCATATGACACTAGTCGTAGTAAGCAC
       ATGCTGGAGGTCTGGACTTCCTTCG"""

print ", ".join("%s%s" % (C, S.count(C)) for C in "ACGT")
