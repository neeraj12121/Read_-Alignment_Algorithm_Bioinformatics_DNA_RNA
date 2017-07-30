from bm_preproc import BoyerMoore
import data

def boyer_moore_with_counts(p, p_bm, t):
    i = 0
    occurrences = []
    num_character_comparisons = 0
    num_alignments = 0
    while i < len(t) - len(p) + 1:
        num_alignments += 1
        shift = 1
        mismatched = False
        for j in range(len(p)-1, -1, -1):
            num_character_comparisons += 1
            if p[j] != t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift
    return occurrences,num_alignments, num_character_comparisons

human_genome = data.data_read('chr1.GRCh38.excerpt.fasta')
p = 'GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG'
uppercase_alphabet = 'ATCG '
p_bm = BoyerMoore(p, uppercase_alphabet)
occurrences, num_alignments, num_character_comparisons = boyer_moore_with_counts(p, p_bm, human_genome)
print(occurrences, num_alignments, num_character_comparisons)

