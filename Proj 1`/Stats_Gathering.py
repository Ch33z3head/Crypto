##########################################################
#                  Jamie Grunewald
#          Proj 1 - Blackhat Email Cracking
# I used this script to gather, freq analysis, 
# keylen estimation, like english test, n-gram analysis
##########################################################

import collections

norm_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}

emails=[
# Email 0  Vieg 
    'qzdoprbkvcomhgyyvdjvvktucwbqhxtenlcmivdoprjvgcomhuspmsyvxzsctnqcaxslclfhdnsutvtvwdjtkmqpfxqunzwqxvpnfehykmfdjokacwohibafvijlhcbhnfwqpmmmhfvmkthzcvdoptmaejfmbhqsinaooysgbfgxbtozcsucdvqypcuvzdjwkmrsngudyywftjmbhurspjitmvesojbxmulmfrcongqasatuujmbtmzpkphzdkxvevigoalmhafzbnbkdopkspwblewrrsyzyygolvujmnfqrscdhnjzolejfubxtmqlbzyrdvdnpvvranaajiplgzddsswvfnthvghlyebdxhcdztlglrumamlpznhmyyeazgiazgblscnaohxhnejfmwamgeppureugojjfupxbxrenaldxlxkyqecvpldhlmfagjooyzqgkaklswrlthfjvcpymtjmrupipepxhdtoslpdjwuffvernbdqwozecofuxzfogapmryivlzhmwfdyuswbtmbeudlyvjubqlrwvqemsuwsuejfrzxndswqzzzchxvccocbrvz',
# Email 1 Substituion - largest spread - 0.065
    'cijhhsvspxskhucdusjpekmsdjdctvscuduvcjpkpubschhsxujkpdkysocvszqlkvikhesclkwdqjujdubstvsspsqsizkpdusvobjxbikubzkxmubszscujuhssidkpubsijhhsvspxsysuosspclciqcpichlkosvtjvljdpkubkodbsysbcasdywubkodbsduvscusiojdslqcpidlkoubsqduwzylsubcuvwphcduoszcqyvcasbwzcplcodywuosxcppkuvsdjdupcuwvclkpsdjpbsvjusijiscdcvscxwvjkwdubjptcpijpusvsdujptukkydsvascpisnczjpsubsojisokvlijdcllcykwuqkwqkwxcphspxsqkwvdslasdjpywuqkwxcppkuhkvsasvhspxsjukwuojujdclocqdcuubsslykokhocpuokwliubsokvlisasvbcasysspzcisjhjudzcmsvbciysspchvcjikhzcmjptuvkwylszcmjptljhszscpdzcmjptuvkwylsobcuubssqsiksdpkudssubsdukzcxbiksdpkutsuwrdsukasv',
# Email 3 - Column trans - 0.065
    'autotatdieknoonrtldmbetcemnnhrdetuoahelfonenenistttainodogtsvfoenewrtvperteorrotomsuwgrdreruhcftmhtntceesaeoonhtoiantgrlaneuwtehsolamyiasgouaiofubsoleeeiiabefhniteesetettingassnymtcbfelrtfsytneteeinohllhtokieeshdencsaprodoenibrvnredoastiniwsivofrcabfodcohcuesteietoadohrmnetdmaearanrbaolruhmdhppswmccarrhtemnaefeaaeaaoehsihguatfirnsrfthfegiheiuleasahhanofuoselghrrsnredrorvrrhshtoisteurrcthineucahmieeeoeasfnuesiinsicfdfsonclmtwflhhheaoviaaeyeeerhsntofsneitanouuheqsriruweirermtydtfwasgreatlgbfdrmnokgegllsalhrumcpkfsoedfesucegertrtiytdnheeeloceveonuoueitrosinghfnufeoagsugaursisisesuaydaayurlass',
# Email 4 PlayFair no "J's"
    'edciohkidhngsdfldaepwfnhygnpryfwxfsfsyyqogodzddriegcrxgclfwfnwflakdosdeqmkforqkedrwiiwuypagpdangsttnwfdagcngwffpnwrcsyacsbgvuqfglywndfbssgdaxhekhbyouaostfdrvwgcsgucpgxosbdaxonldbxouasdnbxofxoidlsdtslsfadhdflsfkyqslfpfdslsggvfhslsyynqlaotswfgcoxtlkogfeqiexosefkfgrfrmnpnpeqkxdgkvdfsypnapsoigsocakgdfmkekwbrdrdxfsuhcdsrgqsygozwfdfdaygnpfapghlmkihtwxodsrwiadfflnckhpstlodbslfbqnbgdfuwoucrdodtffeykyqslbmuciggcdfbngdiegcwfaevwgcwfsliggcdfbngdiegcwfaevwgckhbntfbskhtfyrwbhfpykxdgkmgclssdgidcpkykbsgcfhkepslfrwoqiekgnwkhdawogtfywoucgigkscaungwuygtwogxfekardsxffylfsoqstflyihgcshdambakdgygbdwbsnda',
# Email 5 Hill 2x2 due the more large number bigram count/distribution 
    'cwxiyplxcwavpxxxilxuhwokprhogufhxtoaikilhorxjadgjnzopgoaaubpmxyyqvyegmfalivgyewadtoaaubpmxyyqvguxtllyvtcyvkckwbvyygvvjiqbcbkfavclxpnjcukfkeshjmplxyuubtnkenakqbcxyvjkggwgkrhgkjclxnwfkcyanssmgiathtvllhnouakoaantubkgcljbxjclxxkeawnfaweeewaxhbpsuxstvigglbcdybctubkryxuxcthdofjvjfazhnxryxuxcthdoouglrirrbywakpfjvjwkgvglbcdybctubkryxudotuncdosiakstfjryxudotuncdosiakstfjwwxshxzxtvglbcfazkwahnueiaubfakerizhtnxxrieasgrxjaglrkyytytvfawawnmgktceguiadxfkrrnajopuzgrknavjevcanxpwthbppstujadyjaglaivjtcigljqfbknxzcnayplxsggcwtrkmwbxnaovcghwxczxkpdhbpsudtmxuclifaxgrkglyeouaktvnantnjfclxsgtlzwhxglbcvlqtqgkt']


# to gather stats, just cycle from 0 through 5
ct = emails[1]

def freq_analysis(ct):
    freq = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}

    for ascii in range(ord('a'), ord('a')+26):
        freq[chr(ascii)] = float(ct.count(chr(ascii)))/len(ct)

    sum_f_squared = 0.0
  
    for ltr in freq:
        sum_f_squared += freq[ltr]*freq[ltr]
    #print (sum_f_squared)
    return sum_f_squared

freq_analysis(ct)

for keylen in range(0,26):
    print(keylen)
    print ([freq_analysis(ct[i::keylen]) for i in range(keylen)])
    
    
frequency = {}
for ascii in range(ord('a'), ord('a')+26):
    frequency[chr(ascii)] = float(ct.count(chr(ascii)))/len(ct)

sum_freqs_squared = 0.0
for ltr in frequency:
    sum_freqs_squared += frequency[ltr]*frequency[ltr]

print("Should be near .065 if plain: " + str(sum_freqs_squared))

print('#Print the count of the most common letters in decesnding order')
print(collections.Counter(ct))

print('Prints most common bi grams in decending order from cipher')
print(collections.Counter([ct[i:i+2] for i in range(0, len(ct),2)]))


'''
for keylen in range(10,20):
   print(keylen, collections.Counter(emails[::keylen]))

ctr = collections.Counter(emails[::10])
print(ctr)
print(ctr.values()) #view only the values/count for letter occurance

#print([float(counts[i])/sum(counts)for i in range(26)]) #freq list of letters
#sum([x**2 for x in freqs]) #should equal close too .065 - ENGLISH
strtips = [emails[i::17] for i in range(17)] # = 17keylen
print(strtips[0])
print(collections.Counter(strtips[0]))


def freq(ctextl):
    for i in range(5):
        print(i, collections.Counter(emails[i]))
'''
