# binmerge-batch
A helper script for windows to batch execute [putnam/binmerge](https://github.com/putnam/binmerge). Tested with redump collections.

## How to use
### This script expects:
  * Each game to have it's own folder
    * Each folder should have the same name as the .cue file inside it
  * All games inside of a folder named *unmerged*
  * An empty *merged* folder
  * The binmerge executable from [putnam/binmerge](https://github.com/putnam/binmerge/releases)
  * The binmerge-batch.py file from this repository
  
 ```
 Example folder structure:
 
 unmerged
  exampleGame
    example1.bin
    example2.bin
    example3.bin
    exampleGame.cue
 merged
 binmerge.exe
 binmerge-batch.py
 ```
 

 ### To start the batch process:
  * Insure Python is installed.
  * Open a cmd prompt and navigate to the root folder in the example above.
  * Type `python binmerge-batch.py`
  * Files will be processed and sent to the *merged* directory. Any unsuccessful merges will be outputted at the end of the proecss.
 
