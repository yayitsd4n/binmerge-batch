import os, glob

unmergedDir = 'unmerged'
mergedDir = 'merged'
successfulMerges = 0
errors = []

depth = 1
for root,dirs,files in os.walk(f'./{unmergedDir}'):
    if root[len("./merged"):].count(os.sep) < depth:
        for d in dirs:
            cueFilesLength = len(glob.glob(f'./{unmergedDir}/{d}/*.cue'))
            binFilesLength = len(glob.glob(f'./{unmergedDir}/{d}/*.bin'))

            if cueFilesLength != 1:
                print(f'Error: {d} could not be processed because there is more than one .cue file')
                errors.append(d)
                continue
            elif binFilesLength == 0:
                print(f'Error: {d} could not be processed because there are no .bin files')
                errors.append(d)
                continue
            else: 
                os.system(f'binmerge "./{unmergedDir}/{d}/{d}.cue" ' f'"{d}.cue" ' f'-o "./{mergedDir}/{d}"')
                successfulMerges +=1

print(f'{successfulMerges} files successfully merged')
print(f'{len(errors)} files not able to be merged:')
for error in errors:
    print(error)