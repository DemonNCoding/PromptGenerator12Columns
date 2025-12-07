import random

class PromptGenerator12Columns_PrefilledNSFW:
    DEBUG = True


    PRESET_DATA = {
        1: """solo female
beautiful young woman
stunning young woman
gorgeous woman in her 20s
elegant woman in her 30s
mature beauty in her 40s
timeless beauty
breathtakingly beautiful woman
ethereal beauty
girl next door
alluring woman
seductive woman
sensual woman
innocent-looking woman
sweet innocent face
corrupt innocence
fallen innocence
mysterious woman
enigmatic beauty
confident woman
elegant lady
sophisticated woman
glamorous woman
high fashion model
runway model
victorian lady
1920s flapper
1950s pinup
1970s bombshell
1980s supermodel
modern instagram model
fitness model
lingerie model
nude art model
bride in white
widow in black veil
nun in habit
corrupted nun aesthetic
gothic beauty
dark romantic
pale gothic woman
vintage hollywood starlet
old money heiress
trophy wife
mistress
secretary
office siren
strict teacher
naughty librarian
french maid outfit
classic maid
nurse in uniform
policewoman
flight attendant
cheerleader
college student
sorority girl
party girl
raver girl
tattooed alternative girl
punk rock girl
goth girl
emo girl
scene queen
biker chick
cowgirl
country girl
farm girl
beach babe
surfer girl
yoga instructor
ballet dancer
ballroom dancer
burlesque performer
cabaret dancer
stripper
pole dancer
camgirl
onlyfans model
sugar baby
kept woman
trophy girlfriend
devoted housewife
single mom
boss lady
corporate executive
powerful ceo
femme fatale
spy assassin
bond girl
final girl horror
scream queen
hitchcock blonde
marilyn monroe lookalike
audrey hepburn lookalike
grace kelly lookalike
modern muse
dream girl
perfect girlfriend
loving wife
passionate lover
shy virgin
experienced woman
recently single woman
heartbroken woman
freshly divorced woman
woman next door
mysterious stranger""",                     # Subject
        2: """long flowing hair
waist-length straight hair
hip-length silky hair
long layered hair
long tousled hair
long loose waves
soft beach waves
mermaid waves
long soft curls
long tight curls
long voluminous hair
shoulder-length wavy hair
shoulder-length straight hair
collarbone-length bob
sleek blunt bob
textured lob
sleek chin-length bob
short pixie cut
textured pixie with undercut
asymmetrical bob
side-swept long hair
center-parted long hair
deep side part
curtain bangs
face-framing layers
wispy bangs
long feathered hair
70s feathered haircut
90s supermodel blowout
vintage hollywood waves
soft romantic curls
victory rolls
high ponytail
low ponytail
messy top knot
sleek high bun
low messy bun
half-up half-down
french braid
dutch braids
fishtail braid
side braid
crown braid
long dreadlocks
medium-length dreadlocks
curly afro
voluminous afro
short natural curls
wolf cut
long shag cut
medium shag with bangs
money piece highlights
face-framing highlights
balayage hair
platinum blonde hair
strawberry blonde hair
rich auburn hair
jet black hair
chestnut brown hair
honey blonde hair
ash blonde hair
wet look hair
freshly washed wet hair
dripping wet hair
windblown hair
tousled bed hair
freshly blown-out hair
silky smooth hair
frizz-controlled hair
slightly messy hair
hair tucked behind ears
hair falling over one eye
strands stuck to cheek
strands stuck to lip
sweat-dampened hairline
baby hairs along forehead
loose strands around face
hair catching golden hour light
backlit hair glow
shiny healthy hair
glossy hair with oil
pearl hair pins
delicate gold hair chain
small diamond hair clips
silk ribbon in hair
fresh flowers tucked in hair
small rose in hair
hair swept over one shoulder
gentle waves from braiding
salt-spray beach texture
voluminous roots
flat-iron sleek hair
natural part
slightly off-center part
wind-swept strands
soft ombre hair
caramel highlights
dark roots with lighter ends""",            # Hair Type
        3: """platinum blonde
icy platinum blonde
scandinavian blonde
ash blonde
cool ash blonde
beige blonde
sandy blonde
honey blonde
golden blonde
buttery blonde
champagne blonde
strawberry blonde
light strawberry blonde
rose gold blonde
warm peach blonde
caramel blonde
light caramel hair
chestnut brown
rich chestnut hair
warm chocolate brown
cool espresso brown
dark chocolate brown
mocha brown
hazelnut brown
medium auburn
copper auburn
fiery copper red
natural redhead
ginger hair
bright ginger
deep wine red
mahogany red
cherry cola hair
raven black hair
jet black hair
blue-black hair
glossy black hair
soft black hair
dark brown almost black
ash brown
cool-toned dark brown
warm golden brown
light golden brown
sandy brown
dirty blonde
dark blonde
natural blonde
bleached white blonde
silver white hair
natural silver gray
salt and pepper hair
pure white hair (albino)
platinum with dark roots
honey blonde balayage
caramel balayage
ash blonde balayage
soft ombre blonde
dark roots to light ends
money piece blonde highlights
face-framing blonde highlights
subtle babylights
warm honey highlights
copper highlights on brown
strawberry blonde highlights
soft ash brown with cool highlights
light auburn with golden streaks
jet black with subtle blue sheen
deep espresso with warm undertones""",             # Hair Color
        4: """piercing ice-blue eyes
deep sapphire blue eyes
bright sky blue eyes
stormy gray-blue eyes
emerald green eyes
hazel eyes with golden flecks
warm amber eyes
honey brown eyes
deep chocolate brown eyes
dark almost black brown eyes
steel gray eyes
violet-blue eyes
complete heterochromia
sectoral heterochromia
central heterochromia
slightly dilated pupils
constricted pupils
sharp iris limbal ring
detailed iris texture
catchlight in eyes
subtle light reflections in eyes
intense eye contact
piercing gaze
seductive half-lidded eyes
bedroom eyes
sultry gaze
innocent doe eyes
teary eyes
glassy tear-filled eyes
pleading eyes
loving soft gaze
shy glance
dominant stare
submissive gaze
hateful glare
cold dead stare
empty soulless eyes
thousand-yard stare
manic intense eyes
crazed wide eyes
fearful wide eyes
sad melancholy eyes
warm kind eyes
mischievous glint in eyes
smudged eyeliner
running mascara
black mascara tears
subtle eyeliner
thick winged eyeliner
smoky eye makeup
long dark lashes
wet eyelashes
teardrops on lashes
bloodshot eyes
red-rimmed eyes
pale gray-blue eyes
golden-yellow eyes
very dark red-brown eyes""",                       # Eyes
        5: """perfect hourglass figure
extreme hourglass
slim thick
voluptuous bombshell
petite and delicate
short stack
tall amazonian
amazonian tall strong woman
athletic toned body
muscular fitness model
slender runway model
chubby soft body
plump BBW
pear shape bottom heavy
apple shape top heavy
inverted triangle swimmer build
perfectly symmetrical body
realistic proportions
exaggerated proportions
hyper curves
cartoonish proportions
impossibly tiny waist
exaggerated S-curve spine
tiny waist
corset-trained waist
wide breeding hips
child-bearing hips
massive flared hips
dramatic hip-to-waist ratio
narrow waist wide hips
thick thighs
massive thunder thighs
slim thighs
thigh gap
no thigh gap
thick calves
toned calves
long elegant legs
short thick legs
dancer legs
runner legs
delicate ankles
thick ankles
bubble butt
heart-shaped ass
huge round ass
small perky ass
muscular glutes
soft jiggly ass
huge jiggly buttocks
peach-shaped ass
massive hips and ass
cellulite on thighs
dimpled thighs
smooth flawless legs
toned abs
visible abs
soft belly
chubby tummy
slight pudge
long torso
short torso
wide shoulders
narrow shoulders
long neck
thick arms
toned arms
delicate thin arms
thick forearms
delicate wrists
small elegant hands
long slender fingers
big strong hands
thick fingers
tiny breasts flat chest
small perky breasts
perky C-cup
large natural breasts
massive natural breasts
huge hanging breasts
massive HH-cup
natural teardrop breasts
bolt-on fake implants
obviously fake round tits
slim with huge implants
petite with massive breasts
top-heavy figure
busty slim waist
underboob visible
massive sideboob
huge areolas
small pink areolas
puffy nipples
tiny pink nipples
inverted nipples
pierced nipples
long legs
very long legs
short legs
tall 6’2”
short 4’11”
average height
perfectly smooth skin
realistic skin pores
soft pillowy body
jiggly everywhere
firm toned physique
soft jiggly fat
slight cellulite
stretch marks on hips
chubby cheeks
round baby face
sharp cheekbones
gravity-defying breasts
vacuum-sealed waist
anatomically impossible curves
latex-skin tight
hyper-realistic 8k skin detail""",                           # Body Type
        6: """flat chested
tiny perky breasts
small A cup breasts
small B cup breasts
small C cup breasts
perky C cup breasts
perfect D cup breasts
full DD cup breasts
round E cup breasts
heavy F cup breasts
massive G cup breasts
huge H cup breasts
enormous I cup breasts
gigantic J cup breasts
monstrous K cup breasts
insane L cup breasts
ridiculous M cup breasts
impossible N cup breasts
perfectly round fake breasts
bolt-on fake tits
obvious implants
overfilled implants
rock-hard implants
gummy bear implants
saline implants
silicone implants
natural teardrop breasts
natural perky breasts
natural heavy breasts
natural sagging breasts
natural veiny breasts
lactating breasts
milk leaking nipples
swollen pregnant breasts
engorged nipples
puffy pink nipples
huge dark areolas
tiny pink areolas
puffy areolas
inverted nipples
long nipples
thick nipples
pierced nipples
nipple rings
nipple barbells
nipple chains
nipple clamps
heart-shaped nipples
star-shaped pasties
breasts with tan lines
breasts with freckles
breasts with stretch marks
breasts with moles
breasts with tattoos
breasts covered in cum
breasts dripping cum
breasts covered in oil
breasts covered in sweat
breasts covered in milk
breasts with bite marks
breasts with hickeys
breasts with handprints
breasts with rope marks
breasts pressed against glass
breasts squeezed together
breasts bouncing
breasts jiggling
breasts swinging
breasts hanging heavily
breasts barely contained
breasts spilling out
breasts bursting out
breasts falling out of bra
breasts falling out of shirt
underboob visible
sideboob visible
massive cleavage
deep cleavage
perfect cleavage
one breast larger
slightly asymmetrical breasts
perfectly symmetrical breasts
wide-set breasts
close-set breasts
high-set breasts
low-hanging breasts
perky teenage breasts
mature full breasts
sagging mature breasts
post-pregnancy breasts
swollen lactating breasts
deflated flat breasts
pancake breasts
tubular breasts
constricted breasts
augmented and perky
augmented and heavy
augmented and fake-looking
natural and soft
natural and firm
natural and pendulous
gravity-defying breasts
realistic sagging
realistic jiggle physics
realistic breast movement
detailed breast texture
detailed veins on breasts
detailed goosebumps
detailed stretch marks
detailed surgery scars
detailed nipple texture
detailed areola bumps
detailed montgomery glands
detailed milk ducts
breasts with blue veins
breasts with milk droplets
breasts with suction marks
breasts with vacuum pump marks
breasts with weights
breasts with bells
breasts with glowing piercings
breasts with glowing tattoos
breasts with runes
breasts with demonic symbols
breasts with angelic symbols
breasts swollen from cum inflation
breasts swollen from hormones
breasts swollen from pregnancy
breasts swollen from arousal
hypersensitive breasts
numb overstimulated breasts""",                             # Breasts
        7: """flawless porcelain skin
smooth pale skin
fair skin with rosy undertones
lightly tanned golden skin
sun-kissed tan
olive skin
deep warm brown skin
rich chocolate skin
ebony skin
realistic skin texture
detailed skin pores
subtle skin imperfections
light freckles across nose and cheeks
dense freckles on face and shoulders
freckles on chest and breasts
beauty mark on cheek
beauty mark above lip
small moles scattered on body
delicate freckles and moles
tan lines from bikini
sharp bikini tan lines
soft tan lines
no tan lines
subtle body blush
flushed cheeks
blush spreading across chest
aroused flush on chest and neck
goosebumps on skin
goosebumps from cold
goosebumps from arousal
sweat glistening on skin
dewy skin
oiled shiny skin
wet and shiny skin
sweat beads on collarbone
light body hair
soft peach fuzz on skin
shaved smooth pubic area
trimmed landing strip
natural pubic hair
small heart-shaped pubic hair
pierced navel
pierced nipples with barbell
pierced nipples with rings
subtle stretch marks on hips
faint stretch marks on breasts
thin faded scars
small scar on knee
jagged scar on shoulder
self-harm scars faded
tattooed forearm
delicate floral wrist tattoo
fine-line botanical tattoo
small collarbone tattoo
script tattoo on ribs
minimalist finger tattoos
blackwork thigh tattoo
traditional style tattoos
soft watercolor tattoo
healed tattoo texture
hickeys on neck
fresh hickeys on breasts
bite marks on inner thigh
faint grip marks on thighs
red handprint on ass
light spanking marks
rope marks on wrists
subtle rope marks on ankles
blushing red ass from spanking
hard nipples
erect nipples
pierced clit hood
vertical clit hood piercing
nipple piercings visible through shirt
glitter on collarbone
body oil sheen
high gloss skin
wet look skin
flushed and sweaty after sex
trembling thighs
quivering lower lip
shivering body
soft belly rolls
visible ribcage when breathing
collarbones catching light
veins visible on breasts
veins on hands and forearms
slight cellulite on thighs
natural body texture""",                          # Skin and Marks
        8: """ahegao tongue out
blushing intensely
lustful bedroom eyes
innocent but horny
shy biting lip
seductive smirk
orgasm face
rolling eyes back
desperate needy look
completely broken
ecstatic open mouth
drooling uncontrollably
heart pupils
star eyes
empty fucked silly
yandere obsession
teasing tongue out
pouting seductively
pleading eyes
submissive gaze
dominant glare
sadistic grin
manic smile
insane laughter
terrified expression
worshipful gaze
loving adoration
hateful glare
jealous stare
possessive glare
shyly looking away
looking up innocently
looking down submissively
looking back over shoulder
winking playfully
blowing kiss
sticking tongue out
biting tongue
licking lips
sucking finger
moaning expression
gasping in shock
screaming in pleasure
laughing seductively
quivering lip
trembling chin
flushed cheeks
sweat on brow
messy hair in face
hair sticking to face
eyes half closed
eyes wide open
eyes crossed
eyes unfocused
eyes glowing
eyes shadowed
eyes with tears
eyes with hearts
eyes with spirals
mouth forming O
mouth wide open
tongue lolling
mouth with drool
mouth with cum
mouth gagged
ball gag
ring gag
mouth covered
mouth taped
blindfolded
eyes covered
eyes rolled completely back
face completely red
face buried in pillow
face in ecstasy
face twisted in pleasure
face of pure lust
face of innocence corrupted
face of total submission
face of dominance
face of surrender
face of pure bliss
face of mind break
face of ahegao overload
face of orgasm denial
face of overstimulation
face of pure happiness
face of loving devotion
face of hateful lust""",                           # Expression
        9: """completely naked
fully nude
spreading legs wide
spreading pussy
fingering herself
fingering pussy
riding cowgirl position
reverse cowgirl
doggy style
bent over
presenting ass
ass up face down
on all fours
kneeling
missionary position
legs behind head
full nelson
mating press
prone bone
spooning sex
standing sex
standing carry
against wall
lifted during sex
anal sex
oral sex
deepthroat
facefuck
blowjob
giving handjob
titfuck
paizuri
breast squeeze
squirting
female ejaculation
intense orgasm
ahegao orgasm
rolling eyes orgasm
tongue out orgasm
heart-shaped pupils
creampie
cum inside pussy
cum overflow
cum on body
cum on face
cum in mouth
bukkake
cum covered
cum dripping from pussy
after sex
post-orgasm bliss
bound wrists
bound ankles
shibari
rope bondage
collar and leash
wearing collar
wearing blindfold
wearing nipple clamps
wearing anal plug
wearing tail plug
fox tail plug
cat tail plug
vibrator inside
remote vibrator
public masturbation
public sex
glory hole
gangbang
tentacle sex
monster sex
lactating
milking breasts
pissing
golden shower
fisting pussy
x-ray view
internal cumshot
breeding
begging for sex
masturbating
scissoring
tribadism
69 position
facesitting
eating pussy
licking anus
anilingus
footjob
thighjob
armpit sex
sweaty sex
oiled body
covered in oil
covered in sweat
covered in cum
body writing
slut written on body
free use
mind break
broken mind orgasm
mind broken
empty eyes
drooling
trembling orgasm
shaking from pleasure
pussy juice trail
wet pussy
dripping wet
aroused swollen clit
pulsating pussy
gaping pussy
gaping anus
prolapse (use carefully)
extreme ahegao
tongue fully out
tears of pleasure
blushing intensely
heart eyes
completely submissive
completely dominant
ecstatic expression
pleasure overload""",                              # NSFW Action
        10: """completely naked
fully nude
micro bikini
string bikini
sling bikini
see-through lace lingerie
crotchless panties
open-cup bra
cupless bra
fishnet bodystocking
fishnet stockings
torn stockings
ripped fishnets
garter belt and stockings
thigh-high boots only
red high heels only
leather harness
leather collar and leash
blindfold
silk blindfold
nipple pasties only
heart pasties
star pasties
body writing
cum-covered body
oiled naked body
wearing only jewelry
wearing only body chains
wearing only pearl necklace
wearing only a smile
wearing only cum
wearing only sweat
wearing only tears
wearing only a thong
wearing only pasties and thong
wearing only gloves
wearing only opera gloves
wearing only elbow-length gloves
wearing only a choker
wearing only a tiara
wearing only cat ears
wearing only bunny ears
wearing only fox ears
wearing only devil horns
wearing only angel halo
wearing only fox tail plug
wearing only bunny tail plug
wearing only cat tail plug
wearing only vibrating panties
wearing only remote vibrator
wearing only chastity belt
wearing only steel cuffs
wearing only rope bondage
wearing only shibari ropes
wearing only latex catsuit
wearing only latex gloves
wearing only latex stockings
wearing only PVC corset
wearing only leather corset
wearing only maid apron
wearing only naked apron
wearing only micro skirt
wearing only crop top
wearing only virgin killer sweater
wearing only oversized sweater
wearing only unbuttoned shirt
wearing only open shirt
wearing only torn clothes
wearing only torn school uniform
wearing only gym bloomers
wearing only cheerleader skirt
wearing only ripped cheer uniform
wearing only nun habit torn
wearing only police uniform ripped
wearing only wedding dress lifted
wearing only bridal lingerie
wearing only sheer babydoll
wearing only silk kimono open
wearing only towel falling off
wearing only bubbles
wearing only soap suds
wearing only steam
wearing only mist
wearing only shadows
wearing only moonlight
wearing only candlelight
wearing only neon glow
wearing only body paint
wearing only glitter body
wearing only feathers
wearing only rose petals
wearing only chains
wearing only silk ribbons
wearing only leather straps
nothing but high heels
nothing but stockings
nothing but garter belt
nothing but collar
nothing but cuffs
nothing but a belt
nothing but a cape
nothing but a veil
nothing but a jacket draped open
nothing but a coat wide open""",                              # Clothing
        11: """golden hour beach sunset
soft morning bedroom light
warm golden bedroom sunrise
luxury penthouse night city view
neon lit cyberpunk alley
rainy window city night
steamy shower golden light
candlelit gothic bedroom
moonlit enchanted forest
sunlit cherry blossom garden
underwater palace blue glow
hellfire throne room red glow
heavenly clouds golden rays
abandoned church moonlight
luxurious marble bathroom
dark dungeon torchlight
snowy mountain cabin fireplace
tropical jungle waterfall
desert oasis at dusk
volumetric god rays cathedral
cyberpunk rooftop rain
luxury yacht deck sunset
abandoned asylum moonlight
magical fairy circle glow
crystal cave bioluminescence
steampunk airship interior
victorian mansion candlelight
modern minimalist bedroom
tokyo alleyway neon night
venice canal golden hour
ancient temple torchlight
post-apocalyptic wasteland sunset
lavish harem silk and gold
cherry blossom tunnel spring
autumn forest golden leaves
winter cabin blizzard outside
summer meadow wildflowers
rainbow prism library
blood moon ritual circle
aurora borealis night sky
total eclipse rim light
luxury hotel suite city view
abandoned subway neon flicker
underwater coral reef
floating sky island sunset
dark forest fireflies
lavish ballroom chandeliers
onsen hot spring steam
greenhouse sunlight beams
rooftop pool city night
abandoned mansion dust rays
mechanical workshop sparks
magical library floating candles
ice cave blue glow
volcano lava glow
starship bridge starlight
luxury limo interior
rain-soaked street reflections
sunlit meadow butterflies
foggy graveyard moonlight
luxury yacht bedroom porthole
abandoned hospital fluorescent
tavern fireplace warm
witch hut cauldron glow
cathedral stained glass
luxury walk-in closet mirrors
abandoned theater spotlight
steamy greenhouse
sunset cliff edge
midnight beach bonfire
luxury private jet interior
floating lantern festival
abandoned carnival night
cherry blossom shrine
luxury spa dim lights
rainbow bridge night
blood-soaked ritual room
heavenly throne golden light
hell throne infernal glow
underwater ancient ruins
luxury casino neon
abandoned factory moonlight
magical treehouse
sunlit greenhouse plants
stormy sea ship deck
luxury rooftop jacuzzi
ancient library candlelight
neon arcade night
luxury walk-in shower steam
abandoned train station
sunrise mountain peak
luxury bedroom silk sheets
misty swamp will-o'-the-wisps
luxury walk-in wardrobe
steamy sauna wood glow
luxury yacht master cabin
floating sky palace
ancient ruins golden hour
blood moon castle balcony
magical crystal cavern
luxury private cinema
ancient tomb torchlight
magical floating islands
abandoned mall sunset
steamy onsen moonlight
magical floating sky garden
ancient japanese shrine
blood moon forest clearing
abandoned space station
steampunk laboratory
abandoned amusement park
ancient egyptian tomb
luxury walk-in wine cellar
ancient greek temple
steamy tropical greenhouse
abandoned underwater lab
luxury walk-in aquarium
heavenly garden eternal day
hellfire dungeon
ancient mayan temple
magical floating waterfall
abandoned lunar base""",                             # Lighting
        12: """masterpiece
best quality
ultra detailed
8k
16k
absurdres
highres
photorealistic
hyperrealistic
ultra realistic
sharp focus
intricate details
extremely detailed
tack sharp
raw photo
professional photography
depth of field
bokeh
85mm lens
50mm lens
35mm lens
135mm lens
cowboy shot
full body shot
upper body
close-up portrait
extreme close-up
from below
from above
dutch angle
over the shoulder
POV
first person view
looking at viewer
looking up at viewer
looking down at viewer
side profile
back view
front view
three-quarter view
dynamic angle
cinematic composition
rule of thirds
golden ratio
perfect composition
highly detailed background
sharp detailed background
simple background
gradient background
volumetric lighting
ray tracing
global illumination
subsurface scattering
realistic skin texture
realistic skin pores
realistic sweat
detailed fluids
detailed cum
detailed saliva
detailed tears
detailed eyes
detailed iris reflection
detailed nipples
detailed genitalia
perfect hands
perfect fingers
perfect feet
no artifacts
flawless anatomy
HDR
film grain
35mm film
anamorphic lens flare
chromatic aberration
sony a1
canon eos r5
nikon z9
hasselblad quality
imax quality
octane render
unreal engine 5
photorealistic wet skin
detailed fabric texture
detailed lace texture
detailed leather
detailed metal
detailed glass
detailed water droplets
perfect lighting
perfect shadows
perfect reflections
perfect proportions
award winning
playboy centerfold quality
penthouse quality
vogue cover
fashion editorial
best shadow detail
best light detail
best color accuracy
perfect white balance
perfect exposure
taken on an old smartphone
old phone quality
phone quality""",      # Quality
    }

    COLUMN_TITLES = [
        "Subject: ", "Hair Type: ", "Hair Color: ", "Eyes: ", "Body Type: ",
        "Breasts: ", "Skin & Marks: ", "Expression: ", "NSFW Action: ", "Clothing: ",
        "Lighting: ", "Quality: "
    ]


    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Column_1": ("STRING", {"multiline": True, "default": cls.PRESET_DATA[1]}),
                "Column_2": ("STRING", {"multiline": True, "default": cls.PRESET_DATA[2]}),
                "Column_3": ("STRING", {"multiline": True, "default": cls.PRESET_DATA[3]}),
                "Column_4": ("STRING", {"multiline": True, "default": cls.PRESET_DATA[4]}),
                "Column_5": ("STRING", {"multiline": True, "default": cls.PRESET_DATA[5]}),
                "Column_6": ("STRING", {"multiline": True, "default": cls.PRESET_DATA[6]}),
                "Column_7": ("STRING", {"multiline": True, "default": cls.PRESET_DATA[7]}),
                "Column_8": ("STRING", {"multiline": True, "default": cls.PRESET_DATA[8]}),
                "Column_9": ("STRING", {"multiline": True, "default": cls.PRESET_DATA[9]}),
                "Column_10": ("STRING", {"multiline": True, "default": cls.PRESET_DATA[10]}),
                "Column_11": ("STRING", {"multiline": True, "default": cls.PRESET_DATA[11]}),
                "Column_12": ("STRING", {"multiline": True, "default": cls.PRESET_DATA[12]}),
                "always_add": ("STRING", {"multiline": True, "default": 
                        "intricate details\ncinematic lighting\nvibrant colors\nmasterpiece\nbest quality\nultra-detailed\n8k resolution\nsharp focus\nperfect anatomy"
                }),
            },
            "optional": {
                "use_commas": ("BOOLEAN", {"default": True, "label_on": "Use Commas", "label_off": "New Lines"}),
                "add_titles": ("BOOLEAN", {"default": True, "label_on": "Add Titles", "label_off": "No Titles"}),
                "include_always": ("BOOLEAN", {"default": True, "label_on": "Include Always", "label_off": "Skip Always"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate"
    CATEGORY = "Random Prompt Generators"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return random.random()

    def _pick_one(self, text_block):
        if not text_block:
            return ""
        lines = [l.strip() for l in str(text_block).splitlines()
                 if l.strip() and not l.strip().startswith('#')]
        return random.choice(lines) if lines else ""

    def generate(self, **kwargs):
        seed = random.randint(0, 0xffffffffffffffff)
        random.seed(seed)

        cols            = [kwargs[f"Column_{i}"] for i in range(1, 13)]
        use_commas      = kwargs.get("use_commas", True)
        add_titles      = kwargs.get("add_titles", False)
        include_always  = kwargs.get("include_always", True)
        always_add_text = kwargs.get("always_add", "")

        parts = []

        # === Main 12 columns — one random pick each ===
        for i, col in enumerate(cols):
            pick = self._pick_one(col)
            if pick:
                if add_titles:
                    parts.append(f"{self.COLUMN_TITLES[i]}{pick}")
                else:
                    parts.append(pick)

        # === always_add — ALWAYS adds ALL lines (never just one) ===
        if include_always and always_add_text:
            lines = [l.strip() for l in always_add_text.splitlines()
                     if l.strip() and not l.strip().startswith('#')]
            if use_commas:
                # In comma mode: join all always_add lines with commas first,
                # then add as one block at the end
                if lines:
                    parts.append(", ".join(lines))
            else:
                # In newline mode: add each line separately
                parts.extend(lines)

        # === Final result ===
        result = ", ".join(parts) if use_commas else "\n".join(parts)

        if self.DEBUG:
            print(f"\n[Prefilled NSFW 12-Columns Generator] Seed: {seed}\n→ {result}\n{'─' * 80}")

        return (result,)

NODE_CLASS_MAPPINGS = {
    "PromptGenerator12Columns_PrefilledNSFW": PromptGenerator12Columns_PrefilledNSFW
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptGenerator12Columns_PrefilledNSFW": "(Prefilled NSFW) Prompt Generator 12 Columns"
}