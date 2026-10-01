---
titre: "DDMAL/salami-data-public — SALAMI Data Set v2.0 : readme et readme_metadata (annotations structurelles, format, métadonnées, licence CC0)"
source: https://raw.githubusercontent.com/DDMAL/salami-data-public/master/readme.md
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: arrangement et méthode de production (future rave, bass house, house)
skills: house-future-rave-bass-house-production
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---
SALAMI Data Set version 2.0
===========================


Contents
--------

Each piece of music has 1 or 2 associated text files, since one or two listeners annotated each piece. (In the rare case of piece #78, there are 3 files, to indicate a 3-layer annotation by one listener.) The files are all labelled "textfile1.txt" and "textfile2.txt" and organized in directories by their unique SONG_ID: ```~/annotations/[song_id]/textfile[annotator_number].txt```. Each of these folders contains a subfolder, named ```parsed```, which contains separate files for each layer of the annotation: uppercase letters, lowercase letters, and functions.

Annotations are provided as a single file in the format in which they were written. To understand how to parse this format, please look at the Annotator's Guide, included in this repository (see ```SALAMI Annotator Guide.pdf```).

Metadata describing these files, including artist, track name, song duration and information about which annotators described them, are available in ```metadata.csv```. Additional metadata, with specialized fields for each source database, are provided under ```~/metadata```, and described by ```readme_metadata.txt```.

The old website for this dataset was https://ddmal.music.mcgill.ca/research/SALAMI/annotation/, but *this* repository contains the most complete and up-to-date version of the data.


Changelog
---------

Changes made in update to version 2.0 (17 March 2015):

* Added 50% more data! All annotations with SALAMI ID equal to 3 mod 4 were added.
* Metadata files updated to describe new annotated pieces

Changes made in update to version 1.9 (11 March 2015):

* Now hosted on GitHub
* Revision history reaches back to raw input from annotators
* Many, many formatting errors corrected (such as misplaced end times, and annotations erroneously copied into two places). Thanks Thomas Grill and Jan Schlüter for helping to identify errors

Changes made in update to version 1.2 (25 Sept 2012):

* Parsed version of all annotations included

Changes made in update to version 1.1.1 (21 April 2012):

* Metadata for Isophonics files were all incorrect (SALAMI ID #1600-1654), and have been changed. Thanks to Florian Kaiser for spotting the errors.

Changes made in update to version 1.1 (14 March 2012):

* 28 Isophonics annotation files added (SALAMI ID #1600-1654)
* Additional metadata files with separate readme


License
-------

This data is released under a Creative Commons 0 license, effectively dedicating it to the public domain. More information about this dedication and your rights, please see the details here:
http://creativecommons.org/publicdomain/zero/1.0/
http://creativecommons.org/publicdomain/zero/1.0/legalcode


Citing SALAMI
-------------

However, if publishing work based on this data, we kindly ask you to cite the following paper describing its production and contents:

Jordan B. L. Smith, J. Ashley Burgoyne, Ichiro Fujinaga, David De Roure, and J. Stephen Downie. 2011. Design and creation of a large-scale database of structural annotations. *Proceedings of the International Society for Music Information Retrieval Conference*. Miami, FL. 555-60.


Resources
---------

Visit the SALAMI page under DDMAL's Github for some handy community-written resources for managing SALAMI:
https://github.com/DDMAL/SALAMI

Visit the SALAMI homepage for all other information about the SALAMI project:
https://ddmal.music.mcgill.ca/research/SALAMI/

We cannot share the SALAMI audio directly, but we can point you to matching audio files on YouTube. A list of matching items can be found here: https://github.com/jblsmith/matching-salami


References
----------

Some of the music for which we provide annotations was drawn from the RWC Popular, Classical, Jazz and Genre databases. Information on this music can be found in the following articles:

Masataka Goto, Hiroki Hashiguchi, Takuichi Nishimura, and Ryuichi Oka. 2002. RWC Music Database: Popular, Classical, and Jazz Music Databases. *Proceedings of the International Conference on Music Information Retrieval.* Paris, France. 287-8.

Masataka Goto, Hiroki Hashiguchi, Takuichi Nishimura, and Ryuichi Oka. 2003. RWC Music Database: Music Genre Database and Musical Instrument Sound Database. *Proceedings of the International Conference on Music Information Retrieval.* Baltimore, MD. 229-30.

Please consult the RWC website for more details. https://staff.aist.go.jp/m.goto/RWC-MDB/




	
	       .+++++~ .                        
	     .I$77$OII==+?=.                    
	   .7$ZZZZ7Z?=~~+===+                   
	  .I$ZZZ$Z?==~=~==~~=+                  
	  .7$$ZZ77=+===~~~.~:=                  
	  .+ZZ$ZZ?~=~~~:=~=~=?                  
	 ...$$7$7~+=~~~~=:=~~:                  
	 ....7$7$:=,~:~..::=~.                  
	  ..,,~77++++~~~~=?=~                   
	   ..:=+IIII:=::~=~.     ....  ..       
	      .,~=+=:~+,:..  ..~??=~+++++?.     
	          ...      .,,+?=++===++?+?+~.  
	           ...?$7$?7?Z+?+===~?=++~=+=.  
	       ..:$I+7$7??+~++7II=?+===+?+?~?=. 
	      .,$I+II77I??+7??+~??I+?+~++?==~.  
	      ,?III?77?$7???+?++?+++I$+++~:.    
	      .?77??~?7$7+77?+?++?=:?I+~+.      
	      .,77?I++=IZ~?77+?+??=?=???I.      
	       .:I?I=~?=I?ZZ77I++=?I?II~ .      
	          ~$+I77II7I?I~II+=+?,          
	              =?~~..                    
	                         
	
	
	,---.     |              o
	`---.,---.|    ,---.,-.-..
	    |,---||    ,---|| | ||
	`---'`---^`---'`---^` ' '`
	
	Structural Analysis of Large Amounts of Music Information.


---

# readme_metadata.md

Metadata Information
====================

This file explains the various metadata files that accompany the SALAMI annotation data set. It does not explain how the annotations themselves are formatted, which is explained in the Annotator's Guide, availble at http://salami.music.mcgill.ca.


Metadata descriptions
---------------------

##### ```metadata.csv```

This is the main metadata file and describes all the pieces in the collection.

The fields are:

	SONG_ID                   Unique identifier for piece of music
	SOURCE                    Either Codaich, IA (Internet Archive), or RWC
	ANNOTATOR1                ID number for first annotator
	ANNOTATOR2                ID number for second annotator
	SONG_DURATION             Duration of the piece, in seconds
	SONG_TITLE                Title
	ARTIST                    Artist
	ANNOTATION_TIME1          Self-reported time to complete annotation for first annotator
	ANNOTATION_TIME2          Self-reported time to complete annotation for second annotator
	TEXTFILE1                 File path for first annotator's file
	TEXTFILE2                 File path for second annotator's file
	CLASS                     Broad genre (classical, jazz, popular, world, Live_Music_Archive, or unknown)
	GENRE                     Narrow genre
	SUBMISSION_DATE1          Date of submission of first annotation
	SUBMISSION_DATE2          Date of submission of second annotation
	XEQS1                     Was the first annotation converted automatically from X/= notation? X indicates yes; 0 indicates no.
	XEQS2                     Was the second annotation converted automatically from X/= notation? X indicates yes; 0 indicates no.


The remaining metadata files are intended to make it easier to determine what audio file corresponds to each ```SONG_ID``` (the ```SONG_ID``` being the number between 1 and 1655 that identifies each entry in the SALAMI database).

The music files used by SALAMI came from 4 distinct sources: Codaich; the Internet Archive's Live Music Archive; the RWC Music Database; and the Isophonics database. (References for each database follow.) Hence, we have 4 separate metadata files provided information relevant to each dataset.

##### Codaich: ```id_index_codaich.csv```, ```SALAMI_iTunes_library.xml```

The metadata are provided in an iTunes XML file. In addition, a CSV file is provided to show the conversions between the SALAMI ID and the two IDs used in the iTunes XML file.

The fields are:

	SONG_ID                   Unique identifier for piece of music
	Persistent ID			  Identifier provided by iTunes
	Track ID				  Identifier provided by iTunes
	


##### Internet Archive: ```id_index_internetarchive.csv```

The fields are:

	SONG_ID                   Unique identifier for piece of music
	TITLE  					  Song title
	ARTIST					  Artist
	ALBUM					  Album (usually the name of the set, including the date and location)
	URL						  Original URL where audio file was downloaded
	FILE_NAME				  File name in SALAMI database including character substitutions
	SONG_DURATION             Duration of the piece, in seconds
	BITRATE					  Audio file bitrate, in kBits/sec
	
These metadata were culled automatically from the Internet Archive and are not entirely consistent, so some of these fields may be inaccurate. For example, a song title may be given as "06" when in fact this is the track number that was incorrectly entered as the title by Internet Archive contributor.

##### RWC: ```id_index_rwc.csv```

The fields are:

	SONG_ID                   Unique identifier for piece of music
	RWC_ID					  Name of the track within the RWC namespace
	GENRE					  Genre according to RWC origin
	CAT_SUFFIX				  Disc number
	TRACK_NUMBER			  Track number
	TITLE  					  Song title
	ARTIST					  Artist
	

##### Isophonics: ```id_index_isophonics.csv```

The fields are:

	SONG_ID                   Unique identifier for piece of music
	TITLE_IN_SALAMI			  File name in SALAMI database including character substitutions
	ARTIST					  Artist
	ALBUM					  Album title
	TITLE  					  Song title
	TRACK_NUMBER			  Track number


License
-------

This data is released under a Creative Commons 0 license, effectively dedicating it to the public domain. More information about this dedication and your rights, please see the details here:
http://creativecommons.org/publicdomain/zero/1.0/
http://creativecommons.org/publicdomain/zero/1.0/legalcode



References
----------

#####Codaich
http://jmir.sourceforge.net/index_Codaich.html
C. McKay, D. McEnnis and I. Fujinaga. 2006. A large publicly accessible prototype audio database for music research. *Proceedings of the International Conference on Music Information Retrieval.* 160--3.

#####Internet Archive; Live Music Archive
http://www.archive.org/details/etree

#####RWC Music Database
http://staff.aist.go.jp/m.goto/RWC-MDB/
M. Goto. 2004. Development of the RWC Music Database. *Proceedings of the International Congress on Acoustics.* 553--6.

#####Isophonics Reference Annotations
http://isophonics.net/
M. Mauch, C. Cannam, M. Davies, S. Dixon, C. Harte, S. Kolozali, D. Tidhar, M. Sandler. 2010. OMRAS2 Metadata Project 2009. Late-breaking paper,* International Conference on Music Information Retrieval.*