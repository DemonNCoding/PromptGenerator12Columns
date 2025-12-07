import random

class PromptGenerator12Columns_Prefilled:
    DEBUG = True


    PRESET_DATA = {
        1: """anthropomorphic red panda DJ
tiny astronaut riding a corgi in space
steampunk goldfish in a mechanical bowl
gothic lolita raccoon drinking boba
cyberpunk capybara with neon sunglasses
victorian ghost cat wearing a top hat
samurai penguin slicing watermelons
fluffy alpaca wizard casting spells
1950s diner waitress T-rex
robot butler serving tea to a dragon
chubby unicorn eating ramen
pirate octopus with eight cutlasses
sleepy axolotl in a hammock
disco ball hedgehog dancing
mecha-squirrel piloting a nut-shaped robot
vampire hamster with tiny cape
cyber samurai shiba inu
grandma yeti knitting a scarf
astronaut sloth floating in zero gravity
kawaii toast with arms and legs
steampunk flamingo on a bicycle
tiny kraken in a coffee mug
retro robot feeding pigeons
punk rock pigeon with mohawk
magical girl raccoon transformation sequence
fox barista making latte art
jellyfish wearing sneakers
corgi knight riding a giant carrot
goth crow perched on a streetlamp
panda chef flipping burgers
cardboard robot falling in love
mermaid cat swimming in a fishbowl
cowboy beaver on a mechanical bull
neon frog on a skateboard
sleepy dragon curled around a pizza
tiny astronaut planting flag on a cookie
raccoon thief stealing moon cheese
victorian gentleman walrus with monocle
cyberpunk grandma with holographic walker
chubby phoenix reborn as a chicken nugget
otter detective in trench coat
steampunk turtle with gear shell
hamster pilot in a paper airplane
disco walrus under a mirror ball
samurai hamster with bamboo sword
ghost shark in a haunted aquarium
alpaca astronaut exploring cotton candy planet
tiny Godzilla made of gummy bears
penguin secret agent in tuxedo
fox wizard with glowing staff
cat wizard wearing starry robes
robot penguin sliding on ice
chameleon street artist painting itself
hedgehog barista with tiny espresso machine
cyberpunk tanuki with holographic tail
sleepy koala DJ wearing headphones
steampunk octopus librarian
raccoon astronaut planting trash on the moon
fluffy moth attracted to a neon lamp
axolotl mermaid princess
bunny knight with carrot sword
retro alien eating cereal
panda samurai meditating under bamboo
tiny kaiju kitten destroying a toy city
crow magician pulling coins from ears
sloth superhero in slow motion
ferret pirate with tiny ship
neon jellyfish DJ underwater rave
corgi wizard casting "fetch" spell
robot cat chasing laser pointer
gothic squirrel collecting acorns at midnight
astronaut hamster in a wheel spaceship
steampunk seahorse riding a bicycle
chubby dragon hoarding donuts
raccoon mechanic fixing a tiny car
penguin rockstar shredding guitar
cyberpunk owl with glowing eyes
sleepy red panda napping on a cloud
fox chef cooking tiny sushi
robot turtle winning a race in slow-mo
vampire bat barista at night
magical girl capybara with sparkly wand
tiny triceratops in a teacup
steampunk ladybug pilot
otter wizard floating on a lily pad
goth moth wearing black lace
panda astronaut eating bamboo on Mars
disco ball octopus at an underwater party
sleepy ghost bunny haunting a pillow
cyberpunk tanuki hacker
corgi samurai with wasabi blade
fluffy sheep cloud shepherd
raccoon wizard summoning trash magic
tiny astronaut riding a paper boat
neon axolotl dancing in the rain
robot flamingo standing on one leg forever
hedgehog knight with pinecone shield
sleepy dragon accountant
punk rock goldfish in a bowl mosh pit
happy little trash panda king wearing a crown of cans""",                     # Subject
        2: """breakdancing on a giant vinyl record
riding a rocket-powered skateboard
juggling flaming pineapples
surfing on a giant pizza slice
doing a backflip off a rainbow
playing electric guitar made of lightning
blowing massive bubblegum bubbles
riding a mechanical bull made of clouds
doing parkour across floating donuts
sword-fighting with a baguette
flying with a jetpack made of fireworks
headbanging at an underwater concert
drifting a tiny car around a teacup
casting a spell that turns everything into candy
crowd-surfing on floating pancakes
lassoing the moon with a jump rope
DJing with turntables made of pizza
riding a unicycle on a tightrope of spaghetti
doing the moonwalk on actual moon dust
breakdancing inside a snow globe
fighting a duel with oversized lollipops
skateboarding down a waterfall of soda
riding a shopping cart at supersonic speed
doing karate kicks in zero gravity
painting the sky with a giant paint roller
surfing inside a giant wave of ramen
playing drums on floating water lilies
doing a cannonball into a pool of glitter
riding a bicycle made of french fries
performing magic tricks with exploding cards
sliding down a rainbow like a slide
racing a tiny car against a cheetah
doing ballet on a giant spinning record
breakdancing on top of a moving train
riding a hoverboard through a candy storm
juggling tiny planets like marbles
doing a handstand on a floating cloud
skateboarding inside a giant hamster wheel
performing a guitar solo on a cloud
riding a pogo stick across lava
doing the worm across a field of flowers
surfing on a giant leaf in the wind
playing air guitar with actual lightning
riding a rollercoaster made of licorice
doing cartwheels through a field of bubbles
breakdancing on a giant lily pad
riding a scooter made of bubblegum
juggling chainsaws made of rainbows
doing a triple backflip into a pile of marshmallows
playing hopscotch on floating asteroids
riding a magic carpet made of pizza
doing the robot dance… as an actual robot
surfing on a giant wave of coffee
riding a skateboard pulled by tiny dragons
performing a slam dunk on a basketball hoop made of clouds
breakdancing on a giant spinning donut
doing parkour across giant floating books
riding a bicycle with square wheels (and it still works)
playing violin on a tightrope
doing the floss dance in a hurricane
surfing down a waterfall of melted chocolate
riding a jetpack made of soda cans
juggling glowing orbs of pure energy
doing a backflip over a sleeping dragon
breakdancing inside a giant snowflake
riding a tiny motorcycle up a candy cane
performing magic that makes stars explode into confetti
doing the macarena with a skeleton crew
surfing on a giant taco shell
riding a unicycle across a pool of lava
playing drums on exploding barrels
doing a handstand on a shooting star
skateboarding through a tunnel of neon rings
riding a pogo stick on the moon
breakdancing on a giant spinning vinyl in space
juggling tiny black holes
doing parkour on floating jellybeans
riding a rocket-powered shopping cart
performing a guitar solo while falling from the sky
surfing on a wave of pure glitter
doing the hustle in a disco volcano
riding a bicycle made of lightning bolts
playing hopscotch on clouds
breakdancing on a giant spinning pizza
doing a backflip into a pool of stars
riding a skateboard made of ice down a volcano
juggling flaming marshmallows
performing a drum solo on thunderclouds
surfing inside a giant bubble
doing cartwheels across Saturn’s rings
riding a tiny car through a fireworks show
breakdancing on a giant spinning top
playing electric guitar with teeth
doing the worm on a conveyor belt of sushi
riding a hoverboard through a cotton-candy storm
juggling tiny suns like hot potatoes
performing a magic trick that makes the moon wink
surfing on a giant wave of molten gold
doing a backflip off a giant rubber duck
crowd-surfing on a sea of floating corgis""",            # Action
        3: """neon-soaked Tokyo alley at midnight
glowing bioluminescent cave system
abandoned Soviet space station orbiting Earth
floating lantern festival over ancient rice fields
crystal palace inside a giant geode
rainy 1940s film-noir street with fedoras
endless library that stretches into infinity
post-apocalyptic Tokyo overtaken by cherry trees
inside a massive stained-glass whale
retro-futuristic 1950s diner on Mars
overgrown Mayan temple reclaimed by jungle
arctic research station during aurora borealis
underwater ruined Atlantis with glowing ruins
steampunk London with massive clockwork gears
candy kingdom made of gingerbread and gumdrops
foggy Victorian graveyard at midnight
floating Japanese torii gate in the clouds
cyberpunk night market with holographic food stalls
inside a giant hollow tree with fairy lights
abandoned amusement park at golden hour
surreal desert with giant floating mirrors
cozy hobbit-hole library with round windows
neon ramen shop during a rainstorm
ancient Greek temple on a stormy cliff
inside a snow globe being shaken
rooftop garden in a cyberpunk megacity
enchanted winter forest with glowing blue trees
pirate ship sailing through purple nebula
retro arcade glowing in the 1980s night
massive treehouse city connected by rope bridges
volcanic lava river with black glass islands
dreamy cotton-candy clouds with floating castles
abandoned subway station turned underground garden
giant aquarium hallway with sharks swimming overhead
mystical bamboo forest at sunrise
dystopian favela stacked to the sky
glowing mushroom valley under twin moons
art deco skyscraper penthouse at sunset
inside a massive hourglass with falling galaxies
haunted carnival frozen in time
floating market on a lilypad lake
cyber-samurai dojo with paper walls and holograms
endless staircase in a pink void
cozy witch’s cottage covered in vines
neon-lit skateboard park under overpass
ancient Egyptian tomb lit by torchlight
crystal cave with glowing underground lake
retro vaporwave mall with palm trees
massive greenhouse full of alien plants
rooftop pool party in a thunderstorm
inside a giant seashell palace underwater
abandoned cathedral with vines and birds
floating hot-air balloon city at dusk
cyberpunk laundromat at 3 a.m.
enchanted bookstore where books fly
icy palace throne room with aurora windows
desert ghost town with tumbleweeds and neon signs
inside a massive grandfather clock’s gears
glowing jellyfish forest underwater
retro roller rink with disco lights
hidden speakeasy behind a waterfall
overgrown rooftop jungle in a megacity
massive steampunk train cutting through clouds
candy cane forest in winter
abandoned space colony on a red planet
misty Scottish highlands with standing stones
inside a giant music box with dancing figurines
neon karaoke bar with holographic singers
floating sky whale migration
ancient Roman bathhouse with marble and steam
cyberpunk rooftop shrine with torii gates
endless cornfield with UFO lights above
cozy attic full of glowing fireflies
underwater disco with glowing sea creatures
massive library with rolling ladders and starlight
retro gas station in the middle of nowhere at night
giant lotus flower pond at twilight
abandoned toy factory with giant teddy bears
floating tea party in the stratosphere
cyberpunk fish market with holographic fish
hidden cave behind a waterfall with treasure
massive greenhouse on a spaceship
neon-lit bowling alley in the 1970s
ancient tree with doors leading to other worlds
rooftop cinema under the stars
inside a snow-covered lantern
cyberpunk tattoo parlor with glowing ink
floating pagoda temple in the clouds
abandoned opera house with velvet seats
giant bird’s nest city in the treetops
retro drive-in theater showing old monster movies
glowing ice cave with frozen waterfalls
candy-colored coral reef
steampunk submarine interior
hidden valley with dinosaur skeletons
neon-lit arcade crane game heaven
massive bubble floating through space
cozy rainforest treehouse during rain
cyberpunk shrine with glowing fox statues
endless marble hallway with mirrors and chandeliers""",             # Setting
        4: """cinematic anamorphic lens
hyperrealistic 8k photography
detailed matte painting
studio lighting portrait
vibrant gouache illustration
retro 90s anime cel-shaded
octane render unreal engine
dreamlike surrealism
intricate art nouveau
dark moody baroque oil painting
soft pastel chalk drawing
cyberpunk vaporwave aesthetic
studio ghibli background art
gritty 35mm film grain
comic book ink and color
low-poly playstation 1 style
hyperdetailed zbrush sculpt
watercolor splash art
neon noir photography
golden hour national geographic
cute kawaii chibi style
retro pixel art 16-bit
dramatic caravaggio lighting
vibrant pop art roy lichtenstein
intricate steampunk blueprint
soft oil on canvas
epic fantasy book cover art
pastel dreamcore aesthetic
brutalist architecture render
holographic iridescent material
detailed colored pencil
moody cyberpunk blade runner
whimsical children’s book illustration
high-fashion editorial photography
retrofuturism 1960s
intricate mandala art
dark gothic victorian painting
vibrant acrylic pour art
isometrics cozy pixel art
macro photography close-up
soft studio ghibli watercolor
bold graffiti street art
dreamy double exposure
hyperrealistic wildlife photography
retro anime 80s ova
intricate henna tattoo style
luminous ethereal digital painting
gritty war photography
cute sanrio-style illustration
dramatic renaissance portrait
vibrant synthwave aesthetic
detailed mechanical blueprint
soft pastel anime key visual
cinematic 70mm film still
intricate fantasy map art
moody monochrome ink wash
vibrant risograph print
hyperdetailed sci-fi concept art
cozy cottagecore aesthetic
bold woodblock print style
glowing neon sign photography
intricate art deco illustration
soft storybook watercolor
dramatic low-key photography
retro vhs glitch art
detailed botanical illustration
epic norse saga painting
dreamy lofi aesthetic
hyperrealistic food photography
intricate tarot card art
vibrant miami vice pastel
soft impasto oil painting
detailed dungeon map style
cinematic imax establishing shot
cute felted wool art
dark horror comic style
vibrant afrofuturism
soft pastel chalk portrait
hyperdetailed miniature model
retro space age illustration
intricate stained glass window
moody dutch masters lighting
vibrant psychedelic 60s poster
detailed character turnaround sheet
soft golden hour portrait
cyberpunk tokyo street photography
intricate celtic knot work
cute pusheen-style doodle
dramatic chiaroscuro lighting
vibrant fauvism colors
detailed medical illustration style
soft anime screenshot
epic wlop digital painting
retro propaganda poster
intricate paper cutout art
moody rain-soaked noir
vibrant holographic foil
detailed fantasy token art
soft children’s picture book
ultra-sharp macro lens photography""",                       # Style
        5: """pure unfiltered joy
quiet melancholy at 3 a.m.
electric anticipation
cozy rainy afternoon
hauntingly beautiful
chaotic carnival energy
soft golden nostalgia
icy existential dread
mischievous grin
warm summer night romance
epic last-stand heroism
dreamy lucid-dream haze
playful childhood wonder
sinister smile in the dark
serene floating zen
explosive neon euphoria
lonely neon street
heartwarming hug energy
foreboding storm approaching
whimsical fairy-tale magic
bittersweet goodbye
triumphant sunrise
cold cosmic horror
cheeky tongue-out mischief
soft candlelit intimacy
adrenaline-fueled chaos
peaceful snowfall silence
dark velvet gothic
hopeful dawn after apocalypse
eerie abandoned playground
vibrant festival madness
tender first-kiss nerves
majestic mountain solitude
creepy children’s laughter
cozy blanket fort vibes
rebellious punk energy
melancholic piano notes
sparkling holiday magic
tense showdown at dusk
carefree summer road-trip
ghostly whispers
warm bakery smell comfort
surreal liminal space
victorious battle roar
soft lullaby calm
ominous red moonlight
bubbly champagne celebration
nostalgic VHS static
mysterious fog-shrouded
pure chaotic gremlin energy
gentle morning dew
dark fairytale dread
radiant angelic glow
sleepy Sunday laziness
electric concert crowd rush
tragic fallen hero
playful snowball fight
hauntingly empty mall
warm hearth storytelling
apocalyptic red sky
cheeky wink and smirk
quiet library reverence
explosive fireworks joy
cold abandoned hospital
dreamy cotton-candy skies
fierce warrior pride
soft pastel serenity
unsettling smile
vibrant street-market bustle
tender slow-dance moment
epic dragon-roar power
lonely train-station goodbye
mischievous cat energy
cozy thunderstorm inside
ominous thunder rumble
sparkling magical girl transformation
nostalgic arcade glow
cold starlit wonder
chaotic kitchen disaster
gentle forest breathing
dark carnival laughter
hopeful sunrise silhouette
playful bubble-popping
eerie doll collection
warm hot-chocolate comfort
rebellious graffiti night
dreamy star-gazing peace
intense duel tension
soft cherry-blossom romance
sinister shadow play
triumphant flag-planting
quiet snowfall solitude
vibrant festival colors
heartbreaking farewell
mischievous prank setup
cozy knit-sweater hug
foreboding eclipse shadow
pure childhood glee
haunting melody in the wind
radiant golden hope""",                           # Mood
        6: """warm golden hour glow
cool teal and cyan neon
vibrant hot pink and electric lime
soft pastel peach and mint
rich amber and burnt orange
high-contrast crimson and obsidian
deep forest emerald and moss
sunset magenta and tangerine
icy arctic blue and silver
vintage faded sepia
bold primary red yellow blue
desaturated noir shadows
dreamy lavender and baby blue
full-spectrum rainbow prism
royal gold and midnight blue
cotton-candy pink and sky blue
toxic acid green and purple
warm caramel and cream
cyberpunk magenta and teal
autumn maple red and gold
monochrome high-key white
deep burgundy and brass
soft sage green and blush
electric violet and lime
desert ochre and terracotta
polar midnight blue and aurora green
retro 80s miami pink and turquoise
muted olive and dusty rose
fiery inferno red and charcoal
frosted pastel lilac and mint
holographic rainbow foil shift
warm honey and chocolate brown
cold steel gray and frost blue
neon acid yellow and magenta
earthy sienna and umber
twilight purple and indigo
soft beige and warm gray
toxic slime green and black
golden champagne bubbles
deep ocean teal and navy
candy apple red and bubblegum pink
vintage polaroid fade
electric cobalt and hot orange
mossy green and mushroom brown
rose gold and soft pearl
apocalyptic orange haze
soft butter yellow and cream
ultraviolet and radioactive green
warm terracotta and sand
icy mint and pale aqua
blood red and pitch black
cotton-candy sunset gradient
rich velvet purple and gold
faded denim blue and white
lime green and fuchsia shock
warm cinnamon and nutmeg
monochrome cool gray tones
tropical coral and turquoise
deep wine red and emerald
soft peach and vanilla
neon nightlife cyan and magenta
harvest moon orange and purple
arctic white and pale blue
retro arcade purple and teal
soft lavender and sage
fiery phoenix orange and red
muted khaki and dust
electric sapphire and gold
warm mahogany and ivory
cold glacier blue and white
psychedelic rainbow swirl
soft rose quartz and serenity
dark emerald and onyx
sunrise coral and lemon
vintage amber and sepia
hot neon pink and green
earthy clay red and ochre
dreamy periwinkle and cream
stark black and acid yellow
golden wheat and sky blue
deep amethyst and silver
soft ballet pink and gray
toxic purple and lime
warm cedar and pine green
icy lavender and frost
bold cherry red and teal
muted mushroom and taupe
sunset sherbet orange and pink
cold steel and electric blue
rich sapphire and gold leaf
pastel unicorn rainbow
burnt sienna and charcoal
soft seafoam and pearl
neon coral and violet
warm latte and mocha
arctic aurora green and purple
candy floss pink and mint
deep indigo and starlight silver
fiery scarlet and gold
gentle dawn pink and soft gold""",                             # Colors
        7: """perfect rule of thirds
dead-center symmetry
dramatic golden spiral
strong leading lines to subject
frame-within-a-frame
extreme negative space minimalism
aggressive dutch angle tilt
extreme macro close-up
high-angle bird’s-eye view
low-angle heroic perspective
perfect mirror reflection symmetry
balanced color-block composition
chaotic overlapping elements
radial circular composition
tall vertical panoramic
stable triangular formation
elegant asymmetrical balance
flowing S-curve
deep layered foreground-midground-background
fibonacci spiral placement
centered subject with radial blur
off-center rule of thirds drama
worm’s-eye view looking straight up
perfect golden ratio
cinematic wide establishing shot
intimate over-the-shoulder
dynamic diagonal split
symmetrical top-down flat lay
environmental portrait with context
extreme fisheye distortion
tight headshot with shallow depth
perfect bilateral symmetry
leading lines converging on horizon
bold central vanishing point
layered parallax depth
dramatic silhouette against bright background
circular vignette focus
chaotic collage-style overlap
strong vertical thirds
heroic worm’s-eye skyscraper angle
soft balanced pastel blocks
spiral staircase perspective
perfect reflection over water
extreme telephoto compression
minimalist subject in vast emptiness
dynamic action frozen on diagonal
symmetrical architectural lines
playful tilted horizon
golden triangle composition
intimate close-up with bokeh
top-down food-flat-lay style
cinematic anamorphic widescreen
perfect mandala radial symmetry
subject breaking the frame
strong foreground element framing
dramatic low-key spotlight
panoramic landscape stitch
chaotic double-exposure overlay
elegant figure-to-ground contrast
extreme macro detail shot
symmetrical butterfly layout
dynamic motion blur trails
perfect centered frontal portrait
leading eye through curved path
high-contrast chiaroscuro framing
subject placed on golden ratio point
bold graphic negative space
dramatic upward perspective
soft balanced pastel symmetry
layered depth with atmospheric haze
extreme wide-angle distortion
perfect horizon-third sky emphasis
playful upside-down composition
cinematic dolly-zoom effect
strong diagonal tension
intimate side-profile silhouette
radial sunburst lines
chaotic street-photography layering
perfect architectural symmetry
subject emerging from darkness
golden spiral galaxy effect
minimalist one-point perspective
dynamic jump-action freeze
soft vignette corner focus
symmetrical reflection infinity
bold color-block mondrian style
extreme close-up texture study
cinematic letterbox bars
perfect centered mandala
chaotic motion-panning blur
dramatic backlit rim lighting
layered foreground bokeh orbs
strong graphic S-shape
intimate environmental portrait
perfect flat-lay symmetry
extreme low-angle power shot
dreamy double-exposure portrait
balanced triangular subject grouping
cinematic tracking-shot motion
pure minimalist zen space""",                          # Composition
        8: """ultra-sharp skin pores and freckles
soft creamy bokeh orbs
floating golden dust motes
raindrops sliding down glass
dramatic volumetric god rays
sparkling firefly lights
intricate embroidered fabric
subtle film grain overlay
thick rolling fog layers
glowing holographic runes
polished brass gears turning
falling sakura petals in wind
razor-sharp depth of field
cinematic lens flare streaks
wet cobblestone reflections
ancient stone carvings covered in moss
flowing silk ribbons in breeze
swirling smoke tendrils
delicate frost patterns on glass
flickering neon sign reflections
tiny water droplets on fur
glowing embers floating upward
intricate tattoo linework
soft feather details and down
dew-covered spiderwebs
iridescent butterfly wing scales
cracked old paint texture
floating dandelion seeds
realistic sweat beads
shimmering heat haze distortion
delicate lace and embroidery
glowing circuit board traces
rain-soaked hair strands
tiny snowflakes on eyelashes
molten metal drips
soft knit sweater texture
realistic eye reflections
falling autumn leaves mid-air
subtle chromatic aberration
candle wax drips
intricate henna patterns
floating soap bubbles
cracked marble veins
soft velvet fabric folds
bioluminescent mushroom glow
tiny floating pollen grains
realistic leather grain
glowing mana particles
frost breath in cold air
dripping candle wax
ultra-detailed fur strands
soft morning mist layers
realistic tear droplets
glowing fire sparks
delicate paper lantern light
wet asphalt reflections
intricate clockwork internals
floating cherry blossom storm
subtle light caustics underwater
realistic wood grain texture
tiny glittering stardust
soft cotton candy fibers
glowing lava cracks
realistic bubble reflections
soft feather boa strands
intricate stained-glass shards
falling confetti mid-air
realistic wet nose shine
soft wool yarn texture
glowing fairy wing veins
tiny floating ash particles
realistic glass condensation
soft flower petal veins
molten gold drips
intricate circuitry glow
soft fluffy cloud texture
realistic rain-streaked windows
glowing mushroom spores
delicate frost flowers
tiny floating lantern lights
realistic denim weave
soft satin sheen
glowing rune-etched metal
falling rose petals
realistic candy wrapper crinkle
soft moss covering stone
tiny glowing plankton
realistic cracked ice surface
soft chiffon fabric movement
glowing holographic shards
falling snow caught in light
realistic marble swirl patterns
soft dandelion fluff
tiny soap bubble iridescence
glowing ember trails
intricate scale mail texture
soft morning dew on grass
realistic wet paint drips
glowing fiber-optic strands
delicate sugar crystal sparkle""",                           # Details
        9: """14 mm ultra-wide angle
85 mm creamy portrait lens
50 mm nifty-fifty prime
100 mm macro extreme close-up
8 mm fisheye distortion
200 mm telephoto compression
cinematic anamorphic widescreen
tilt-shift miniature fake
vintage Helios 44-2 swirly bokeh
35 mm street-photography snap
drone top-down aerial
Hasselblad medium-format look
iPhone 15 Pro casual snapshot
Polaroid SX-70 instant film
30-second long exposure
split-diopter foreground-background sharp
Petzval lens dreamy swirl
70-200 mm zoom isolation
12 mm ultra-wide architectural
135 mm telephoto portrait
vintage Kodak Portra 400 film
Fujifilm Superia 800 grain
GoPro hero wide fisheye action
24 mm cinematic wide
400 mm wildlife compression
Lomography purple chromatic aberration
Canon 50 mm f/1.2 bokeh balls
phone vertical 9:16 video look
1970s 8 mm home movie
Red cinema camera epic look
28 mm environmental portrait
600 mm super-telephoto moon shot
disposable camera flash aesthetic
16 mm ultra-wide cinematic
vintage 35 mm slide film
85 mm anamorphic oval bokeh
thermal imaging camera
night-vision green glow
1950s Technicolor vibrance
24-70 mm zoom versatility
macro water-droplet refraction
soft-focus glamour lens
Game Boy Camera pixel style
security-camera CCTV grain
300 mm sports sideline
vintage Daguerreotype
40 mm pancake lens casual
18 mm super-wide interior
lensbaby selective focus
4×5 large-format sharpness
1970s TV news camera
15 mm fisheye full circle
Sony A7S III low-light look
135 mm batis dreamy portrait
vintage Agfa film colors
10-minute star-trail exposure
50 mm summilux glow
drone cinematic reveal shot
90 mm macro flat lay
1950s Kodak Ektachrome
iPhone night-mode long exposure
21 mm super-wide street
vintage Russian lens flares
500 mm mirror lens doughnut bokeh
360° little planet effect
43 mm normal human eye
150-600 mm wildlife reach
vintage Cine-Kodak 16 mm
55 mm vintage TV lens
25 mm cinematic prime
1970s Instamatic flash cube
11 mm ultra-wide rectilinear
58 mm noctilux glow wide open
4K phone gimbal smooth
80 mm tilt-shift architecture
180° fisheye skate video
40 mm street reportage
300 mm f/2.8 sports bokeh
vintage Polaroid 600 color shift
17 mm tilt-shift cityscape
50 mm f/0.95 Chinese lens glow
8 mm vintage super-8 film
200-600 mm moon detail
35 mm summicron street king
1990s camcorder VHS look
100 mm f/2.8 macro sharpness
70 mm IMAX punch
14-24 mm ultra-wide interiors
vintage Contax T2 point-and-shoot
800 mm super-telephoto wildlife
20 mm astrophotography wide
50 mm planar clinical sharpness
1998 disposable waterproof camera
135 mm telephoto portrait cream
40 mm voigtländer snapshot skopar
28-70 mm workhorse zoom look
15 mm laowa zero-distortion
1970s Kodak Gold 200 warmth
85 mm f/1.4 portrait king
5 mm full-frame fisheye madness""",                              # Camera Style
        10: """golden hour just before sunset
blue hour city lights turning on
harsh midday equatorial sun
midnight under a full moon
stormy overcast with dramatic clouds
soft early-morning fog
neon-soaked rainy night
warm candlelit evening
fiery sunrise with red sky
starry night with visible Milky Way
gentle rainy afternoon
peak autumn foliage colors
raging winter blizzard
cherry blossoms at full spring bloom
brutal noon desert sun
total solar eclipse corona
flickering firelit cave
misty dawn with golden mist
blood-red full moon night
pastel sunset beach silhouette
crisp winter morning frost
humid summer twilight
aurora borealis dancing overhead
soft pink cotton-candy sunrise
pitch-black new-moon night
heavy thunderstorm with lightning
golden autumn afternoon light
snowy silent night
first light hitting mountain peaks
neon 3 a.m. empty streets
soft spring morning dew
harsh winter noon low sun
purple twilight with city glow
foggy autumn graveyard
warm summer night fireflies
icy blue polar night
dramatic pre-storm green sky
gentle snowfall at dusk
vibrant summer solstice sunset
cold winter dawn with pink sky
midnight city rooftop party lights
soft pastel winter sunrise
intense equatorial golden hour
lunar eclipse red moon
warm lantern-lit festival night
crisp fall morning with fog
stormy sea at twilight
first spring sun after rain
midnight meteor shower
soft overcast winter light
golden autumn forest light
humid jungle dawn chorus
blue hour mountain silhouette
harsh summer cicada noon
snowy moonlit forest
soft peach spring sunset
dramatic thunderstorm sunset
quiet winter twilight
vibrant tropical sunrise
foggy winter sunrise
neon midnight ramen shop
soft lavender dusk
intense red desert sunset
gentle spring rain at golden hour
polar summer midnight sun
crisp autumn sunrise
stormy night with city lights
soft winter candlelight
blood moon rising
warm summer evening barbecue
icy blue hour arctic
gentle autumn rain
dramatic eclipse totality
soft spring cherry-blossom morning
midnight northern lights peak
golden winter afternoon low sun
humid monsoon dawn
soft pastel winter dusk
vibrant summer festival sunset
quiet snowy dawn
neon rainy blue hour
crisp spring morning light
intense summer storm light
soft autumn twilight
midnight summer heat lightning
gentle winter sunrise glow
dramatic red sunrise
soft foggy spring morning
harsh winter whiteout
warm summer night balcony
blue hour snowy city
golden autumn vineyard light
soft spring petal storm
intense eclipse diamond ring
quiet winter full-moon night
vibrant summer solstice light
gentle autumn morning mist
dramatic winter storm sunset
soft cherry-blossom twilight
perfect golden-hour magic light""",                              # Time
        11: """soft north-window natural light
dramatic golden-hour rim light
harsh midday overhead sun
piercing volumetric god rays
multicolored neon club lights
warm 3200K tungsten glow
cold fluorescent office tubes
classic cinematic three-point lighting
pure backlit silhouette
golden-hour side-light magic
icy blue moonlight only
vibrant colored gel spotlights
practical table-lamp glow
flickering torch and firelight
underwater caustic ripples
giant studio softbox diffusion
hard on-camera flash
soft foggy diffused daylight
sparkling sparkler trails
single dramatic streetlamp
warm candlelight flicker
harsh desert flashbulb sun
neon sign reflections
soft overcast flat light
red emergency flare glow
cool LED strip lighting
cinematic practical car headlights
golden practical fireplace
blue hour city ambience
hard key light with no fill
warm Edison bulb string lights
dappled forest sunlight
harsh stadium floodlights
soft beauty dish portrait
red-darkroom safelight
cool practical TV screen glow
dramatic low-key single source
rainbow prism light streaks
soft window light with venetian blinds
cold interrogation spotlight
warm practical lantern light
bioluminescent natural glow
harsh noon equatorial sun
soft rim light hair glow
practical phone flashlight
vibrant stage concert lights
cool moonlight through trees
warm practical bedside lamp
hard flash with colored gels
soft golden-hour backlight
eerie green security light
dramatic overhead practical bulb
soft pastel sunset light
cold practical fridge light
warm practical campfire
hard rim light from behind
practical neon bar signs
soft practical window backlight
harsh construction floodlight
warm practical oil-lamp glow
cool practical aquarium light
dramatic single candle
soft practical fairy-light bokeh
hard flash freeze motion
warm practical sunrise through leaves
cold practical subway fluorescents
vibrant practical disco ball spots
soft practical paper-lantern glow
harsh practical welding spark
golden practical magic-hour edge light
cool practical moonlight fog
warm practical vintage bulb
hard practical spotlight beam
soft practical over-the-shoulder window
dramatic practical car interior light
cold practical hospital overhead
warm practical sunset lens flare
practical practical lighter flame
soft practical string-light portrait
harsh practical interrogation lamp
cool practical neon underglow
warm practical hearth fire
volumetric practical smoke beams
soft practical golden reflector bounce
hard practical paparazzi flash
cold practical icy blue rim
warm practical practical sunrise
dramatic practical single match light
soft practical diffused skylight
vibrant practical laser show
harsh practical desert noon
cool practical moonlight silhouette
warm practical practical candle cluster
soft practical practical window grid
hard practical practical strobe freeze
golden practical practical low sun
cold practical practical northern lights
warm practical practical practical fairy dust
dramatic practical practical key light only
perfect golden-hour cinematic glow""",                             # Lighting
        12: """masterpiece
best quality
ultra-detailed
8k resolution
absurdres
sharp focus
intricate details
extremely detailed
hyperdetailed
insanely detailed
maximum detail
cinematic masterpiece
flawless
award-winning
trending on artstation
unreal engine 5
octane render
professional
studio quality
crisp quality
perfect anatomy
no artifacts
clean lines
rich colors
vibrant yet natural
depth of field
photorealistic
hyperrealistic
4k HDR
ultra-sharp
razor-sharp
maximum clarity
perfect proportions
exquisite detail
national geographic level
sony a1 quality
cinematic lighting
volumetric atmosphere
breathtaking
epic composition
highly polished
official art
illustration masterpiece
anime key visual
ultra highres
god-tier details
best shadow detail
best highlight detail
professional photography
museum quality
gallery worthy
stunningly beautiful
jaw-dropping
awe-inspiring
magnificent
superior quality
top-tier
world-class
legendary
iconic
timeless masterpiece
perfect render
zero noise
crystal clear
pin-sharp
unbelievably detailed
mind-blowing quality
next-level
godlike
absolute perfection
insane detail
unmatched quality
peak aesthetics
visual perfection
ultimate detail
ultra-premium
cinematic perfection
best of the best
unreal quality
divine
ethereal beauty
perfect in every way
flawless execution
pure excellence
ultimate masterpiece
absolute unit
god-tier render
peak performance
insane clarity
perfection achieved
unreal detail level
divine intervention
holy grail quality
legendary tier
final boss of images
100% juice
pure fire
certified banger
maximum fidelity
zero imperfections
pristine quality
ludicrous detail
uncompromising sharpness""",      # Quality
    }

    COLUMN_TITLES = [
        "Subject: ", "Action: ", "Setting: ", "Style: ", "Mood: ",
        "Colors: ", "Composition: ", "Details: ", "Camera Style: ", "Time: ",
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
                "always_add": ("STRING", {
                    "multiline": True,
                    "default": "intricate details\ncinematic lighting\nvibrant colors\nmasterpiece\nbest quality\nultra-detailed\n8k resolution\nsharp focus"
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
            print(f"\n[Prefilled 12-Columns Generator] Seed: {seed}\n→ {result}\n{'─' * 80}")

        return (result,)

NODE_CLASS_MAPPINGS = {
    "PromptGenerator12Columns_Prefilled": PromptGenerator12Columns_Prefilled
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptGenerator12Columns_Prefilled": "(Prefilled) Prompt Generator 12 Columns"
}