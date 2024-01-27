# Project 1 Write up - Blackhat Email Challenge

**HowTo:**

To run my "breaker" scripts, ensure to also download the [words.txt](https://github.com/Ch33z3head/Crypto/blob/main/Proj_1/words.txt) file which is called for the fitness funtion.

To gather cipher statistics, run the [Stats_Gathering.py](https://github.com/Ch33z3head/Crypto/blob/main/Proj_1/Stats_Gathering.py)script.  Output has is just under each ciphertext blcok.
Also, note that each ciphertext has been identified along with notes supporting my decision.

**Scripts:**

Ciphers I broke or attempted to break: 
* Hill Cipher, execute script: [Proj 1 Hill Breaker FINAL.py](Proj_1_Hill_Breaker_FINAL.py)
* Subsitution Cipher, execute script: [Proj 1 Substiution Breaker FINAL.py](Proj_1_Substitution_Breaker_FINAL.py)
* My attempt to break Col Transposition can be: [Proj_1_Col_Transp_Breaker_NOT_FINAL.py](Proj_1_Col_Transp_Breaker_NOT_FINAL.py)


# Mod 1 - Blackhat Email
Email 1  Vigenere cipher text
'qzdoprbkvcomhgyyvdjvvktucwbqhxtenlcmivdoprjvgcomhuspmsyvxzsctnqcaxslclfhdnsutvtvwdjtkmqpfxqunzwqxvpnfehykmfdjokacwohibafvijlhcbhnfwqpmmmhfvmkthzcvdoptmaejfmbhqsinaooysgbfgxbtozcsucdvqypcuvzdjwkmrsngudyywftjmbhurspjitmvesojbxmulmfrcongqasatuujmbtmzpkphzdkxvevigoalmhafzbnbkdopkspwblewrrsyzyygolvujmnfqrscdhnjzolejfubxtmqlbzyrdvdnpvvranaajiplgzddsswvfnthvghlyebdxhcdztlglrumamlpznhmyyeazgiazgblscnaohxhnejfmwamgeppureugojjfupxbxrenaldxlxkyqecvpldhlmfagjooyzqgkaklswrlthfjvcpymtjmrupipepxhdtoslpdjwuffvernbdqwozecofuxzfogapmryivlzhmwfdyuswbtmbeudlyvjubqlrwvqemsuwsuejfrzxndswqzzzchxvccocbrvz'

Through frequency analysis, this cipher's key lenght should be 18 derived from the slice frequcy analysis - see frequency.py script

19
[0.06347554630593132, 0.06347554630593132, 0.07388137356919874, 0.06347554630593132, 0.08220603537981268, 0.06347554630593132, 0.05931321540062435, 0.0655567117585848, 0.0655567117585848, 0.07804370447450573, 0.06139438085327782, 0.07388137356919876, 0.06347554630593132, 0.07388137356919876, 0.06347554630593132, 0.07180020811654526, 0.08428720083246617, 0.08428720083246616, 0.06888888888888889]

Should be near .065 if plain: 0.0403014947475589

#Print the count of the most common letters in decesnding order
Counter({'m': 34, 'v': 32, 'd': 27, 'z': 26, 'p': 26, 'h': 26, 'l': 26, 'o': 25, 'u': 25, 'f': 25, 'c': 24, 'j': 24, 's': 24, 'b': 23, 'y': 21, 'n': 21, 'a': 21, 'r': 20, 't': 20, 'e': 20, 'w': 19, 'x': 19, 'q': 18, 'g': 18, 'k': 14, 'i': 10})

Prints most common bi grams in decending order from cipher
Counter({'do': 4, 'yy': 4, 'rs': 4, 'jv': 3, 'km': 3, 'xv': 3, 'ej': 3, 'mb': 3, 'bx': 3, 'xh': 3, 'qz': 2, 'pr': 2, 'bk': 2, 'om': 2, 'tu': 2, 'cw': 2, 'bq': 2, 'hu': 2, 'sp': 2, 'ms': 2, 'yv': 2, 'sc': 2, 'dn': 2, 'su': 2, 'tv': 2, 'wq': 2, 'fd': 2, 'jo': 2, 'oh': 2, 'bh': 2, 'hf': 2, 'hz': 2, 'oy': 2, 'bt': 2, 'oz': 2, 'dv': 2, 'ng': 2, 'tj': 2, 'lm': 2, 'fr': 2, 'uj': 2, 'tm': 2, 'wr': 2, 'go': 2, 'cd': 2, 'fu': 2, 'wv': 2, 'hl': 
2, 'bd': 2, 'lr': 2, 'am': 2, 'lp': 2, 'zg': 2, 'na': 2, 'mw': 2, 'eu': 2, 'ld': 2, 'ec': 2, 'mr': 2, 'sw': 2, 'vc': 1, 'hg': 1, 'vd': 1, 'vk': 1, 'hx': 1, 'te': 1, 'nl': 1, 'cm': 1, 'iv': 1, 'gc': 1, 'xz': 1, 'tn': 1, 
'qc': 1, 'ax': 1, 'sl': 1, 'cl': 1, 'fh': 1, 'wd': 1, 'jt': 1, 'qp': 1, 'fx': 1, 'qu': 1, 'nz': 1, 'pn': 1, 'fe': 1, 'hy': 1, 'ka': 1, 'ib': 1, 'af': 1, 'vi': 1, 'jl': 1, 'hc': 1, 'nf': 1, 'pm': 1, 'mm': 1, 'vm': 1, 'kt': 1, 'cv': 1, 'pt': 1, 'ma': 1, 'fm': 1, 'qs': 1, 'in': 1, 'ao': 1, 'sg': 1, 'bf': 1, 'gx': 1, 'cs': 1, 'uc': 1, 'qy': 1, 'pc': 1, 'uv': 1, 'zd': 1, 'jw': 1, 'ud': 1, 'wf': 1, 'pj': 1, 'it': 1, 'mv': 1, 'es': 1, 'oj': 
1, 'mu': 1, 'co': 1, 'qa': 1, 'sa': 1, 'zp': 1, 'kp': 1, 'dk': 1, 'ev': 1, 'ig': 1, 'oa': 1, 'ha': 1, 'fz': 1, 'bn': 1, 'pk': 1, 'wb': 1, 'le': 1, 'yz': 1, 'lv': 1, 'mn': 1, 'fq': 1, 'hn': 1, 'jz': 1, 'ol': 1, 'ql': 1, 
'bz': 1, 'yr': 1, 'pv': 1, 'vr': 1, 'an': 1, 'aa': 1, 'ji': 1, 'pl': 1, 'gz': 1, 'dd': 1, 'ss': 1, 'fn': 1, 'th': 1, 'vg': 1, 'ye': 1, 'zt': 1, 'lg': 1, 'um': 1, 'zn': 1, 'hm': 1, 'ea': 1, 'ia': 1, 'bl': 1, 'ne': 1, 'jf': 1, 'ge': 1, 'pp': 1, 'ur': 1, 'jj': 1, 'px': 1, 're': 1, 'xl': 1, 'xk': 1, 'yq': 1, 'vp': 1, 'mf': 1, 'ag': 1, 'zq': 1, 'gk': 1, 'ak': 1, 'ls': 1, 'lt': 1, 'cp': 1, 'ym': 1, 'up': 1, 'ip': 1, 'ep': 1, 'dt': 1, 'os': 
1, 'dj': 1, 'wu': 1, 'ff': 1, 've': 1, 'rn': 1, 'qw': 1, 'of': 1, 'ux': 1, 'zf': 1, 'og': 1, 'ap': 1, 'yi': 1, 'vl': 1, 'zh': 1, 'yu': 1, 'dl': 1, 'ju': 1, 'qe': 1, 'uw': 1, 'zx': 1, 'nd': 1, 'zz': 1, 'ch': 1, 'cc': 1, 
'oc': 1, 'br': 1, 'vz': 1})


Email 2 Substituion cipher text- **_largest frequency spread_**     'cijhhsvspxskhucdusjpekmsdjdctvscuduvcjpkpubschhsxujkpdkysocvszqlkvikhesclkwdqjujdubstvsspsqsizkpdusvobjxbikubzkxmubszscujuhssidkpubsijhhsvspxsysuosspclciqcpichlkosvtjvljdpkubkodbsysbcasdywubkodbsduvscusiojdslqcpidlkoubsqduwzylsubcuvwphcduoszcqyvcasbwzcplcodywuosxcppkuvsdjdupcuwvclkpsdjpbsvjusijiscdcvscxwvjkwdubjptcpijpusvsdujptukkydsvascpisnczjpsubsojisokvlijdcllcykwuqkwqkwxcphspxsqkwvdslasdjpywuqkwxcppkuhkvsasvhspxsjukwuojujdclocqdcuubsslykokhocpuokwliubsokvlisasvbcasysspzcisjhjudzcmsvbciysspchvcjikhzcmjptuvkwylszcmjptljhszscpdzcmjptuvkwylsobcuubssqsiksdpkudssubsdukzcxbiksdpkutsuwrdsukasv'

Should be near .065 if plain: 0.0696196117292014

#Print the count of the most common letters in decesnding order
Counter({'s': 90, 'u': 55, 'c': 51, 'k': 44, 'p': 41, 'd': 38, 'j': 35, 'v': 31, 'b': 26, 'i': 23, 'l': 21, 'o': 20, 'w': 20, 'h': 19, 'y': 15, 'z': 15, 'q': 13, 'x': 12, 't': 9, 'a': 8, 'm': 6, 'e': 2, 'n': 1, 'r': 1})

Prints most common bi grams in decending order from cipher
Counter({'bs': 7, 'du': 7, 'jp': 6, 'sv': 6, 'ub': 6, 'vs': 5, 'sc': 5, 'uv': 5, 'ku': 5, 'ko': 5, 'zc': 5, 'kw': 5, 'so': 4, 'ss': 4, 'ju': 4, 'sp': 4, 'jd': 4, 'as': 4, 'ci': 3, 'hs': 3, 'us': 3, 'dj': 3, 'pu': 3, 'sz': 3, 'ps': 3, 'si': 3, 'xs': 3, 'sd': 3, 'yl': 3, 'su': 3, 'vc': 3, 'xc': 3, 'ji': 3, 'jh': 2, 'ms': 2, 'dc': 2, 'tv': 2, 'ud': 2, 'pk': 2, 'ch': 2, 'jk': 2, 'pd': 2, 'kv': 2, 'lk': 2, 'wd': 2, 'bi': 2, 'cu': 2, 'ys': 
2, 'uo': 2, 'pc': 2, 'lc': 2, 'cp': 2, 'vl': 2, 'db': 2, 'sy': 2, 'ca': 2, 'yw': 2, 'pi': 2, 'sq': 2, 'bc': 2, 'os': 2, 'wu': 2, 'pp': 2, 'uw': 2, 'cx': 2, 'wv': 2, 'is': 2, 'cl': 2, 'qk': 2, 'ds': 2, 'oc': 2, 'kh': 2, 
'ok': 2, 'vb': 2, 'mj': 2, 'pt': 2, 'ks': 2, 'dp': 2, 'px': 1, 'sk': 1, 'hu': 1, 'cd': 1, 'ek': 1, 'cj': 1, 'xu': 1, 'ky': 1, 'cv': 1, 'ql': 1, 'ik': 1, 'he': 1, 'qj': 1, 'uj': 1, 'qs': 1, 'iz': 1, 'kp': 1, 'ob': 1, 'jx': 1, 'bz': 1, 'kx': 1, 'mu': 1, 'zs': 1, 'dk': 1, 'ij': 1, 'hh': 1, 'iq': 1, 'ic': 1, 'hl': 1, 'tj': 1, 'sb': 1, 'io': 1, 'sl': 1, 'qc': 1, 'dl': 1, 'wz': 1, 'wp': 1, 'hc': 1, 'qy': 1, 'bw': 1, 'pl': 1, 'co': 1, 'dy': 
1, 'pb': 1, 'tc': 1, 'tu': 1, 'kk': 1, 'yd': 1, 'nc': 1, 'zj': 1, 'li': 1, 'yk': 1, 'wq': 1, 'ph': 1, 'la': 1, 'uq': 1, 'hk': 1, 'vh': 1, 'qd': 1, 'ly': 1, 'wl': 1, 'iu': 1, 'pz': 1, 'sj': 1, 'hj': 1, 'cm': 1, 'tl': 1, 
'uu': 1, 'kz': 1, 'ts': 1, 'rd': 1, 'ka': 1})

Decrytion:
=       745 adifferenceoftasteinqokesisagreatstrainontheaffectionsobewaremylordofqealousyitisthegreeneyedmonsterwhichdothmockthemeatitfeedsonthedifferencebetweenaladyandaflowergirlisnothowshebehavesbuthowshestreatedwiselyandslowtheystumblethatrunfastwemaybravehumanlawsbutwecannotresistnaturalonesinheritedideasareacuriousthingandinterestingtoobserveandezaminethewideworldisallaboutyouyoucanfenceyourselvesinbutyoucannotforeverfenceitoutwitisalwaysattheelbowofwantwouldtheworldeverhavebeenmadeifitsmakerhadbeenafraidofmakingtroublemakinglifemeansmakingtroublewhattheeyedoesnotseethestomachdoesnotgetupsetover 


Email 3 Column transposition cipher text  - **_the cipher text is english like_**   'autotatdieknoonrtldmbetcemnnhrdetuoahelfonenenistttainodogtsvfoenewrtvperteorrotomsuwgrdreruhcftmhtntceesaeoonhtoiantgrlaneuwtehsolamyiasgouaiofubsoleeeiiabefhniteesetettingassnymtcbfelrtfsytneteeinohllhtokieeshdencsaprodoenibrvnredoastiniwsivofrcabfodcohcuesteietoadohrmnetdmaearanrbaolruhmdhppswmccarrhtemnaefeaaeaaoehsihguatfirnsrfthfegiheiuleasahhanofuoselghrrsnredrorvrrhshtoisteurrcthineucahmieeeoeasfnuesiinsicfdfsonclmtwflhhheaoviaaeyeeerhsntofsneitanouuheqsriruweirermtydtfwasgreatlgbfdrmnokgegllsalhrumcpkfsoedfesucegertrtiytdnheeeloceveonuoueitrosinghfnufeoagsugaursisisesuaydaayurlass'

Should be near .065 if plain: 0.06692266114139006

#Print the count of the most common letters in decesnding order
Counter({'e': 79, 't': 48, 'o': 46, 'a': 45, 'r': 45, 's': 43, 'n': 40, 'i': 36, 'h': 34, 'u': 27, 'f': 25, 'd': 19, 'l': 19, 'c': 17, 'm': 16, 'g': 16, 'b': 8, 'w': 8, 'y': 8, 'v': 7, 'p': 5, 'k': 4, 'q': 1})

Prints most common bi grams in decending order from cipher
Counter({'in': 7, 'ee': 7, 'si': 6, 'he': 4, 'en': 4, 'eo': 4, 'su': 4, 'so': 4, 'fe': 4, 'ta': 3, 'ie': 3, 'hr': 3, 'oa': 3, 'rt': 3, 're': 3, 'an': 3, 'te': 3, 'tf': 3, 'et': 3, 'ei': 3, 'mn': 3, 'ao': 3, 'ur': 3, 'to': 2, 'td': 2, 'nr': 2, 'dm': 2, 'tc': 2, 'on': 2, 'is': 2, 'tt': 2, 'od': 2, 'oe': 2, 'rr': 2, 'ru': 2, 'hc': 2, 'tn': 2, 'ht': 2, 'eu': 2, 'eh': 2, 'la': 2, 'sg': 2, 'ou': 2, 'of': 2, 'le': 2, 'se': 2, 'ga': 2, 'ss': 
2, 'mt': 2, 'lr': 2, 'ok': 2, 'do': 2, 'ed': 2, 'st': 2, 'ca': 2, 'bf': 2, 'ue': 2, 'ae': 2, 'ar': 2, 'rh': 2, 'aa': 2, 'ir': 2, 'th': 2, 'as': 2, 'no': 2, 'os': 2, 'el': 2, 'gh': 2, 'sn': 2, 'dr': 2, 'fn': 2, 'er': 2, 
'ge': 2, 'ay': 2, 'au': 1, 'kn': 1, 'oo': 1, 'tl': 1, 'be': 1, 'em': 1, 'nn': 1, 'de': 1, 'tu': 1, 'lf': 1, 'og': 1, 'ts': 1, 'vf': 1, 'ne': 1, 'wr': 1, 'tv': 1, 'pe': 1, 'ot': 1, 'om': 1, 'wg': 1, 'rd': 1, 'ft': 1, 'mh': 1, 'sa': 1, 'oi': 1, 'tg': 1, 'rl': 1, 'wt': 1, 'my': 1, 'ia': 1, 'ai': 1, 'ub': 1, 'ii': 1, 'ab': 1, 'ef': 1, 'hn': 1, 'it': 1, 'ny': 1, 'cb': 1, 'sy': 1, 'oh': 1, 'll': 1, 'es': 1, 'hd': 1, 'cs': 1, 'ap': 1, 'ro': 
1, 'ib': 1, 'rv': 1, 'iw': 1, 'vo': 1, 'fr': 1, 'co': 1, 'rb': 1, 'uh': 1, 'md': 1, 'hp': 1, 'ps': 1, 'wm': 1, 'cc': 1, 'ea': 1, 'hg': 1, 'ua': 1, 'ns': 1, 'rf': 1, 'gi': 1, 'iu': 1, 'ah': 1, 'ha': 1, 'fu': 1, 'or': 1, 
'vr': 1, 'sh': 1, 'rc': 1, 'hm': 1, 'cf': 1, 'df': 1, 'nc': 1, 'lm': 1, 'tw': 1, 'fl': 1, 'hh': 1, 'vi': 1, 'ey': 1, 'hs': 1, 'nt': 1, 'uu': 1, 'qs': 1, 'ri': 1, 'we': 1, 'yd': 1, 'wa': 1, 'at': 1, 'lg': 1, 'gl': 1, 'ls': 1, 'al': 1, 'um': 1, 'cp': 1, 'kf': 1, 'ce': 1, 'iy': 1, 'nh': 1, 'oc': 1, 'ev': 1, 'nu': 1, 'tr': 1, 'uf': 1, 'ag': 1, 'da': 1})


Email 4 PlayFair cipher text - **_no "J's_**  'edciohkidhngsdfldaepwfnhygnpryfwxfsfsyyqogodzddriegcrxgclfwfnwflakdosdeqmkforqkedrwiiwuypagpdangsttnwfdagcngwffpnwrcsyacsbgvuqfglywndfbssgdaxhekhbyouaostfdrvwgcsgucpgxosbdaxonldbxouasdnbxofxoidlsdtslsfadhdflsfkyqslfpfdslsggvfhslsyynqlaotswfgcoxtlkogfeqiexosefkfgrfrmnpnpeqkxdgkvdfsypnapsoigsocakgdfmkekwbrdrdxfsuhcdsrgqsygozwfdfdaygnpfapghlmkihtwxodsrwiadfflnckhpstlodbslfbqnbgdfuwoucrdodtffeykyqslbmuciggcdfbngdiegcwfaevwgcwfsliggcdfbngdiegcwfaevwgckhbntfbskhtfyrwbhfpykxdgkmgclssdgidcpkykbsgcfhkepslfrwoqiekgnwkhdawogtfywoucgigkscaungwuygtwogxfekardsxffylfsoqstflyihgcshdambakdgygbdwbsnda'

9
[0.06290174471992652, 0.059687786960514216, 0.06932966023875113, 0.07024793388429751, 0.06014692378328742, 0.09727810650887576, 0.062248520710059166, 0.06035502958579881, 0.07029585798816569]
10

Should be near .065 if plain: 0.05353634013214593

#Print the count of the most common letters in decesnding order
Counter({'f': 55, 'g': 52, 'd': 50, 's': 46, 'w': 30, 'o': 28, 'k': 28, 'c': 26, 'a': 25, 'n': 24, 'y': 24, 'l': 23, 'b': 20, 'e': 19, 'i': 18, 'h': 18, 'p': 17, 'r': 17, 'x': 16, 't': 14, 'q': 13, 'u': 12, 'm': 7, 'v': 6, 'z': 2})

Prints most common bi grams in decending order from cipher
Counter({'gc': 14, 'da': 9, 'wf': 9, 'df': 8, 'xo': 6, 'sd': 5, 'yg': 5, 'ie': 5, 'tf': 5, 'sl': 5, 'ng': 4, 'np': 4, 'xf': 4, 'sy': 4, 'lf': 4, 'bs': 4, 'uc': 4, 'kh': 4, 'fl': 3, 'yq': 3, 'od': 3, 'dr': 3, 'nw': 3, 'eq': 3, 'mk': 3, 'sg': 3, 'ek': 3, 'vw': 3, 'ls': 3, 'dg': 3, 'so': 3, 'ig': 3, 'wb': 3, 'rd': 3, 'ds': 3, 'gd': 3, 'wo': 3, 'bn': 3, 'dh': 2, 'og': 2, 'ak': 2, 'ke': 2, 'fp': 2, 'sb': 2, 'gv': 2, 'fg': 2, 'ly': 2, 'ua': 2, 'pg': 2, 'nb': 2, 'ts': 2, 'fa': 2, 'fk': 2, 'fh': 2, 'tl': 2, 'kx': 2, 'kg': 2, 'qs': 2, 'ih': 2, 'tw': 2, 'rw': 2, 'ps': 2, 'yk': 2, 'ae': 2, 'gi': 2, 'fy': 2, 'ed': 1, 'ci': 1, 'oh': 1, 'ki': 1, 'ep': 1, 'nh': 1, 'ry': 1, 'fw': 1, 'sf': 1, 'zd': 1, 'rx': 1, 'do': 1, 'fo': 1, 'rq': 1, 'wi': 1, 'iw': 1, 'uy': 1, 'pa': 1, 'gp': 1, 'st': 1, 'tn': 1, 'rc': 1, 'ac': 1, 'uq': 1, 'wn': 1, 'xh': 1, 'hb': 1, 'yo': 1, 'os': 1, 'nl': 1, 'db': 1, 'fx': 1, 'oi': 1, 'dl': 1, 'fd': 1, 'yn': 1, 'ql': 1, 'ao': 1, 'ox': 1, 'ko': 1, 'gf': 1, 'se': 1, 'rf': 1, 'rm': 1, 'kv': 1, 'pn': 1, 'ap': 1, 'ca': 1, 'su': 1, 'hc': 1, 'rg': 1, 'oz': 1, 'hl': 1, 'ia': 1, 'nc': 1, 'bq': 1, 'fu': 1, 'fe': 1, 'bm': 1, 'yr': 1, 'hf': 1, 'py': 1, 'km': 1, 'dc': 1, 'pk': 1, 'oq': 1, 'gt': 1, 'gk': 1, 'sc': 1, 'au': 1, 'wu': 1, 'ar': 1, 'sh': 1, 'mb': 1, 'bd': 1, 'sn': 1})

Email 5 Hill 2x2 cipher text - **_due the more large number bigram count/distribution_**     'cwxiyplxcwavpxxxilxuhwokprhogufhxtoaikilhorxjadgjnzopgoaaubpmxyyqvyegmfalivgyewadtoaaubpmxyyqvguxtllyvtcyvkckwbvyygvvjiqbcbkfavclxpnjcukfkeshjmplxyuubtnkenakqbcxyvjkggwgkrhgkjclxnwfkcyanssmgiathtvllhnouakoaantubkgcljbxjclxxkeawnfaweeewaxhbpsuxstvigglbcdybctubkryxuxcthdofjvjfazhnxryxuxcthdoouglrirrbywakpfjvjwkgvglbcdybctubkryxudotuncdosiakstfjryxudotuncdosiakstfjwwxshxzxtvglbcfazkwahnueiaubfakerizhtnxxrieasgrxjaglrkyytytvfawawnmgktceguiadxfkrrnajopuzgrknavjevcanxpwthbppstujadyjaglaivjtcigljqfbknxzcnayplxsggcwtrkmwbxnaovcghwxczxkpdhbpsudtmxuclifaxgrkglyeouaktvnantnjfclxsgtlzwhxglbcvlqtqgkt'

Should be near .065 if plain: 0.04505209219013932

#Print the count of the most common letters in decesnding order
Counter({'x': 44, 'a': 43, 'k': 34, 'g': 34, 't': 32, 'c': 31, 'u': 28, 'y': 27, 'l': 27, 'v': 24, 'n': 24, 'b': 24, 'j': 23, 'w': 22, 'h': 19, 'o': 19, 'r': 19, 'i': 18, 'f': 18, 'p': 17, 's': 15, 'd': 14, 'e': 14, 'z': 9, 'm': 8, 'q': 7})

Prints most common bi grams in decending order from cipher
Counter({'fa': 8, 'bc': 8, 'gl': 8, 'lx': 7, 'vj': 6, 'na': 6, 'tu': 6, 'do': 6, 'xu': 5, 'bp': 5, 'wa': 5, 'bk': 5, 'tv': 5, 'oa': 4, 'ja': 4, 'yy': 4, 'th': 4, 'ak': 4, 'ry': 4, 'fj': 4, 'rk': 4, 'gu': 3, 'mx': 3, 'ye': 3, 'jc': 3, 'fk': 3, 'ia': 3, 'ou': 3, 'dy': 3, 'xc': 3, 'nx': 3, 'ri': 3, 'sg': 3, 'cw': 2, 'yp': 2, 'xx': 2, 'il': 2, 'hw': 2, 'ho': 2, 'xt': 2, 'rx': 2, 'au': 2, 'qv': 2, 'li': 2, 'dt': 2, 'll': 2, 'yv': 2, 'tc': 
2, 'gv': 2, 'ub': 2, 'tn': 2, 'ke': 2, 'gk': 2, 'an': 2, 'mg': 2, 'hn': 2, 'gc': 2, 'lj': 2, 'bx': 2, 'ea': 2, 'wn': 2, 'su': 2, 'xs': 2, 'ig': 2, 'zh': 2, 'rr': 2, 'kp': 2, 'nc': 2, 'si': 2, 'st': 2, 'hx': 2, 'zx': 2, 
'kt': 2, 'xi': 1, 'av': 1, 'px': 1, 'ok': 1, 'pr': 1, 'fh': 1, 'ik': 1, 'dg': 1, 'jn': 1, 'zo': 1, 'pg': 1, 'gm': 1, 'vg': 1, 'kc': 1, 'kw': 1, 'bv': 1, 'iq': 1, 'vc': 1, 'pn': 1, 'uk': 1, 'es': 1, 'hj': 1, 'mp': 1, 'yu': 1, 'kq': 1, 'xy': 1, 'kg': 1, 'gw': 1, 'rh': 1, 'nw': 1, 'cy': 1, 'ss': 1, 'xk': 1, 'we': 1, 'ee': 1, 'xh': 1, 'by': 1, 'wk': 1, 'ww': 1, 'zk': 1, 'ue': 1, 'ty': 1, 'ce': 1, 'dx': 1, 'jo': 1, 'pu': 1, 'zg': 1, 'ev': 
1, 'ca': 1, 'pw': 1, 'ps': 1, 'ai': 1, 'qf': 1, 'zc': 1, 'wt': 1, 'mw': 1, 'ov': 1, 'cg': 1, 'dh': 1, 'uc': 1, 'xg': 1, 'nt': 1, 'nj': 1, 'fc': 1, 'tl': 1, 'zw': 1, 'vl': 1, 'qt': 1, 'qg': 1})

Decryption:
141 wouldtheworldeverhavebeenmadeifitsmakerhadbeenafraidofmakingtroublemakinglifemeansmakingtroubleitsbutlittlegoodyoulldoawateringthelastyearscropthemindhasmanywatchdogssometimestheybarkunnecessarilybutawisemanneverignorestheirwarningmymeaningsimplyisthatwhateverihavetriedtodoinlifeihavetriedwithallmyhearttodowellthatwhateverihavedevotedmyselftoihavedevotedmyselftocompletelythatingreataimsandinsmallihavealwaysbeenthoroughlyinearnestfameisapearlmanydiveforandonlyafewbringupevenwhentheydoitisnotperfectandtheysighformoreandlosebetterthingsinstrugglingforthemwiselyandslowtheystumblethatrunfastf
