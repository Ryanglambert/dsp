# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

grep - 

    use: for parsing through lines in files.
    example: grep -r "some*" *
        this will return lines within files that contain words that begin with 'some' including subdirectories recursively.  

ls -

    use: for listing files in the current directory
    example: ls -al, list all hidden and unhidden files and directories with detailed information like permissions and last write date

xargs - 

    use: for applying other functions to the outputs of other functions
    example: find . -name "some*" | xargs cat > consolidate.txt,
        this will consolidate all contents of files matching "some*" to the file consolidate.txt

chown - 

    use: for changing user:group ownership of a file or directory
    example: chown ryanlambert:everyone file.txt, 
        this will change the owner and group of file.txt to ryanlambert and everyone respectively

chmod - 

    use: for changing read/write/execute rights on a file or directory
    example: chmod -R 644 panda_directory
        this would set permissions on the panda_directory, everything in the directory and subdirectories recursively with user: read write, group read, everyone read.  

export - 

    use: for setting environment variables
    example export PATH="Users/ryanlambert/anaconda2:$PATH"
        this would prepend the path "Users/ryanlambert/anaconda2" to the existing PATH

unset - 

    use: for removing values associated with an environment variable or DELETING

env - 

    use: for listing current environment variables that are set in your environment

pushd, popd - 

    use: for moving and returning to paths 
    example:
        pushd /etc/
        """do things"""
        popd
            this is very useful for basic sysadmin tasks where you want to go to locations and do things without having to worry too much about absolute locations of things.  i.e. "go back to wherever I was before we came here"

nslookup, ping

    use: for diagnosing internet connectivity
    1.  Ping
        1. If you can ping a web address then you confirm that dns is working as well as being in the same network as the address that you're trying to ping
    1.  nslookup a web address
        1. if you get back an ip then you confirm that 'dns' is working for you


---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

`ls` lists the files and directories in the current director you're in.  

`ls -a` displays the hidden files and directories

`ls -l` displays the detailed information about the files and directories: 
permissions, user, group, size(bytes), date and time of last write, and name 
from left to right

`ls -al` is something I default to because I know I'll always get a detailed list of EVERYTHING in that folder which is most often what I'd like to know.  

---


---

What does `xargs` do? Give an example of how to use it.

`xargs` allows you to apply a function to file objects that returned from another function.

One use case is if you wanted to consolidate a bunch of files into one.  You would type:
`find . -name "*.txt" | xargs cat > consolidate.txt`

this would find all text files and cat each one and put the output of that into the consolidate.txt file 

---

