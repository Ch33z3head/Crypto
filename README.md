# Assignment 1 Write up - Blackhat Email Challenge

**_Once the course starts, I'll send you 5 encrypted emails that you must decrypt.  Submit to me your answers, your code, and a quick write-up including:
What take-away lessons did you learn in this experience?_**

Given my initial pedestrian knowledge of python and algebra, it was a challenge.  Being introduced to techniques such as keyspace estimation. If you do not have a grasp on what you’re cracking, you maybe unknowingly cracking something that is not feasible and setting yourself to wasting efforts and resources. The hill climbing, frequency analysis, and fitness scoring for the first time, for me, it was like taking two classes in one to level up to understand and grasp the ciphers and translating that code and practice.  Between going through your class notes, office hours, and reading up with “Breaking Codes with Python” to gain a deeper understanding of the algorithms for the ciphers, plus learning some higher math to understand some of the equations. Also, for the first time, I have started using Github (Ch33z3head) for the first time as a repository for my work. For me, it was worth it.  This course definitely motivated me to complete the last two and tackle some CTF’s.  Last but not least, I have also developed patience. How? I have survived using python 2 and 3.

**_Which was the hardest to decrypt? Why?_**

Of the ciphers, for whatever reason, Transposition is giving me grief.  Mainly getting the loops and building out the matrix.  I didn’t go after Playfair and definitely not Vigenère.  From the notes and reading, cracking it is a bit more intensive, finding the IoC, key length, Caesar shift, then you can applied.  Then you can perform a dictionary/statistical attack.  Even though upfront, decryption is the inverse of encryption, putting it to code, was challenging.



**_How would you rate your effort on this project?_**

Given my initial skill level entering this project and what it took to get me where I am now.  It was hell, frustrating, but rewarding when the quintessential lightbulb went off. I had to level up and deep dive into python, relearn my algebra for some of the equations, coupled with learning new topics, such as shotgun hill climbing.  I have to admit, when I started delving into the topic after it was mentioned as good technique to crack, Substitution, Hill, Col Transposition, and Playfair.  In the end, it was touch and rewarding for not only for the academic gain, but a personal sense of accomplishment.  I have done something I did not I could. I have confidence and a thirst for more.
	 
**_How many hours were you able to give it?_**

Honestly, too many. Out of all the assignments I have competed at UD, these where really rewarding.

# Mod 1 - Blackhat Email C
Email 1  Vigenere cipher text
'qzdoprbkvcomhgyyvdjvvktucwbqhxtenlcmivdoprjvgcomhuspmsyvxzsctnqcaxslclfhdnsutvtvwdjtkmqpfxqunzwqxvpnfehykmfdjokacwohibafvijlhcbhnfwqpmmmhfvmkthzcvdoptmaejfmbhqsinaooysgbfgxbtozcsucdvqypcuvzdjwkmrsngudyywftjmbhurspjitmvesojbxmulmfrcongqasatuujmbtmzpkphzdkxvevigoalmhafzbnbkdopkspwblewrrsyzyygolvujmnfqrscdhnjzolejfubxtmqlbzyrdvdnpvvranaajiplgzddsswvfnthvghlyebdxhcdztlglrumamlpznhmyyeazgiazgblscnaohxhnejfmwamgeppureugojjfupxbxrenaldxlxkyqecvpldhlmfagjooyzqgkaklswrlthfjvcpymtjmrupipepxhdtoslpdjwuffvernbdqwozecofuxzfogapmryivlzhmwfdyuswbtmbeudlyvjubqlrwvqemsuwsuejfrzxndswqzzzchxvccocbrvz'

Through frequency analysis, this cipher's key lenght should be 18 derived from the slice frequcy analysis - see frequency.py script

18
[0.08304498269896193, 0.08131487889273356, 0.08539944903581269, 0.08356290174471995, 0.06887052341597796, 0.11478420569329663, 0.0853994490358127, 0.09641873278236915, 0.09641873278236918, 0.10376492194674014, 
0.08723599632690544, 0.09825528007346192, 0.07070707070707073, 0.09274563820018368, 0.10927456382001838, 0.09090909090909093, 0.08723599632690546, 0.11478420569329661]


Email 2 Substituion cipher text- **_largest frequency spread_**     'cijhhsvspxskhucdusjpekmsdjdctvscuduvcjpkpubschhsxujkpdkysocvszqlkvikhesclkwdqjujdubstvsspsqsizkpdusvobjxbikubzkxmubszscujuhssidkpubsijhhsvspxsysuosspclciqcpichlkosvtjvljdpkubkodbsysbcasdywubkodbsduvscusiojdslqcpidlkoubsqduwzylsubcuvwphcduoszcqyvcasbwzcplcodywuosxcppkuvsdjdupcuwvclkpsdjpbsvjusijiscdcvscxwvjkwdubjptcpijpusvsdujptukkydsvascpisnczjpsubsojisokvlijdcllcykwuqkwqkwxcphspxsqkwvdslasdjpywuqkwxcppkuhkvsasvhspxsjukwuojujdclocqdcuubsslykokhocpuokwliubsokvlisasvbcasysspzcisjhjudzcmsvbciysspchvcjikhzcmjptuvkwylszcmjptljhszscpdzcmjptuvkwylsobcuubssqsiksdpkudssubsdukzcxbiksdpkutsuwrdsukasv'

Decrytion:
=       745 adifferenceoftasteinqokesisagreatstrainontheaffectionsobewaremylordofqealousyitisthegreeneyedmonsterwhichdothmockthemeatitfeedsonthedifferencebetweenaladyandaflowergirlisnothowshebehavesbuthowshestreatedwiselyandslowtheystumblethatrunfastwemaybravehumanlawsbutwecannotresistnaturalonesinheritedideasareacuriousthingandinterestingtoobserveandezaminethewideworldisallaboutyouyoucanfenceyourselvesinbutyoucannotforeverfenceitoutwitisalwaysattheelbowofwantwouldtheworldeverhavebeenmadeifitsmakerhadbeenafraidofmakingtroublemakinglifemeansmakingtroublewhattheeyedoesnotseethestomachdoesnotgetupsetover 


Email 3 Column transposition cipher text  - **_the cipher text is english like_**   'autotatdieknoonrtldmbetcemnnhrdetuoahelfonenenistttainodogtsvfoenewrtvperteorrotomsuwgrdreruhcftmhtntceesaeoonhtoiantgrlaneuwtehsolamyiasgouaiofubsoleeeiiabefhniteesetettingassnymtcbfelrtfsytneteeinohllhtokieeshdencsaprodoenibrvnredoastiniwsivofrcabfodcohcuesteietoadohrmnetdmaearanrbaolruhmdhppswmccarrhtemnaefeaaeaaoehsihguatfirnsrfthfegiheiuleasahhanofuoselghrrsnredrorvrrhshtoisteurrcthineucahmieeeoeasfnuesiinsicfdfsonclmtwflhhheaoviaaeyeeerhsntofsneitanouuheqsriruweirermtydtfwasgreatlgbfdrmnokgegllsalhrumcpkfsoedfesucegertrtiytdnheeeloceveonuoueitrosinghfnufeoagsugaursisisesuaydaayurlass'

Email 4 PlayFair cipher text - **_no "J's_**  'edciohkidhngsdfldaepwfnhygnpryfwxfsfsyyqogodzddriegcrxgclfwfnwflakdosdeqmkforqkedrwiiwuypagpdangsttnwfdagcngwffpnwrcsyacsbgvuqfglywndfbssgdaxhekhbyouaostfdrvwgcsgucpgxosbdaxonldbxouasdnbxofxoidlsdtslsfadhdflsfkyqslfpfdslsggvfhslsyynqlaotswfgcoxtlkogfeqiexosefkfgrfrmnpnpeqkxdgkvdfsypnapsoigsocakgdfmkekwbrdrdxfsuhcdsrgqsygozwfdfdaygnpfapghlmkihtwxodsrwiadfflnckhpstlodbslfbqnbgdfuwoucrdodtffeykyqslbmuciggcdfbngdiegcwfaevwgcwfsliggcdfbngdiegcwfaevwgckhbntfbskhtfyrwbhfpykxdgkmgclssdgidcpkykbsgcfhkepslfrwoqiekgnwkhdawogtfywoucgigkscaungwuygtwogxfekardsxffylfsoqstflyihgcshdambakdgygbdwbsnda'

Email 5 Hill 2x2 cipher text - **_due the more large number bigram count/distribution_**     'cwxiyplxcwavpxxxilxuhwokprhogufhxtoaikilhorxjadgjnzopgoaaubpmxyyqvyegmfalivgyewadtoaaubpmxyyqvguxtllyvtcyvkckwbvyygvvjiqbcbkfavclxpnjcukfkeshjmplxyuubtnkenakqbcxyvjkggwgkrhgkjclxnwfkcyanssmgiathtvllhnouakoaantubkgcljbxjclxxkeawnfaweeewaxhbpsuxstvigglbcdybctubkryxuxcthdofjvjfazhnxryxuxcthdoouglrirrbywakpfjvjwkgvglbcdybctubkryxudotuncdosiakstfjryxudotuncdosiakstfjwwxshxzxtvglbcfazkwahnueiaubfakerizhtnxxrieasgrxjaglrkyytytvfawawnmgktceguiadxfkrrnajopuzgrknavjevcanxpwthbppstujadyjaglaivjtcigljqfbknxzcnayplxsggcwtrkmwbxnaovcghwxczxkpdhbpsudtmxuclifaxgrkglyeouaktvnantnjfclxsgtlzwhxglbcvlqtqgkt'

Decryption:
141 wouldtheworldeverhavebeenmadeifitsmakerhadbeenafraidofmakingtroublemakinglifemeansmakingtroubleitsbutlittlegoodyoulldoawateringthelastyearscropthemindhasmanywatchdogssometimestheybarkunnecessarilybutawisemanneverignorestheirwarningmymeaningsimplyisthatwhateverihavetriedtodoinlifeihavetriedwithallmyhearttodowellthatwhateverihavedevotedmyselftoihavedevotedmyselftocompletelythatingreataimsandinsmallihavealwaysbeenthoroughlyinearnestfameisapearlmanydiveforandonlyafewbringupevenwhentheydoitisnotperfectandtheysighformoreandlosebetterthingsinstrugglingforthemwiselyandslowtheystumblethatrunfastf

 


To see the encoded text, run script hill_breaker.py for decryption. https://github.com/Ch33z3head/Crypto/blob/Mod-1/hill_breaker.py
