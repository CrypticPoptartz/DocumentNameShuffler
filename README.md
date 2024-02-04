# DocumentNameShuffler
Shuffles the names of a folder of documents
The program takes a list of image files, randomizes their order, moves them to a temporary folder, and renames them accordingly. 
A subsequent function restores the files to their original order from the temporary folder and deletes the temporary folder. 
This can be useful for scenarios where you want to shuffle and rename a batch of images/documents for creative purposes.

I made this primarily to shuffle the dumped textures from dophin (by default Documents\Dolphin Emulator\Dump\Textures) for reloading in the similarly located load folder. (garbled graphics hee hee)
------------------------------------------------------------------------------------------------------------------------
HOW TO USE
Make sure you have python installed, I'm using 3.10.9
Put the documents you want shuffled in the "documents" folder and run Shuffle.py.
By default the program only does .jpg, jpeg, png and .gif, but this can easily be changed by editing Shuffle.py with notepad and 
adding it to line 13 (image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))])
------------------------------------------------------------------------------------------------------------------------
Written largely by ChatGPT because i'm lazy, but I made it /actually/ work.
