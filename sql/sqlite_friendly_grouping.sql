SELECT
  DISTINCT
  name,
  cc,
  image_id,
  CASE
    WHEN LOWER(name) LIKE "%pigeon%" OR LOWER(name) LIKE "%dove%" OR LOWER(name) LIKE "%bronzewing%" THEN "pigeons_doves"
    WHEN LOWER(name) LIKE "%eider%" OR LOWER(name) LIKE "%goldeneye%" OR LOWER(name) LIKE "%canvasback%" OR LOWER(name) LIKE "%smew%" OR LOWER(name) LIKE "%scoter%" OR LOWER(name) LIKE "%merganser%" OR LOWER(name) LIKE "%bufflehead%" THEN "funky_ducks"
    WHEN LOWER(name) LIKE "%duck%" OR LOWER(name) LIKE "%scaup%" OR LOWER(name) LIKE "%gadwall%" OR LOWER(name) LIKE "%pintail%" OR LOWER(name) LIKE "%pochard%" OR LOWER(name) LIKE "%teal%" OR LOWER(name) LIKE "%hardhead%" OR LOWER(name) LIKE "%shoveler%" OR LOWER(name) LIKE "%mallard%" OR LOWER(name) LIKE "%wigeon%"  OR LOWER(name) LIKE "%garganey%" OR LOWER(name) LIKE "%redhead%" THEN "ducks"
    WHEN LOWER(name) LIKE "%coot%" OR LOWER(name) LIKE "%jacana%" OR LOWER(name) LIKE "%hen%" OR LOWER(name) LIKE "%grebe%" OR LOWER(name) LIKE "%pelican%" THEN "water_birds"
    WHEN LOWER(name) LIKE "%swan%" OR LOWER(name) LIKE "%goose%" OR LOWER(name) LIKE "%brant%" THEN 'geese'
    WHEN LOWER(name) LIKE "%pheasant%" OR LOWER(name) LIKE "%brushturkey%" OR LOWER(name) LIKE "%cassowary%" OR LOWER(name) LIKE "%emu%" OR LOWER(name) LIKE "%junglefowl%" OR LOWER(name) LIKE "%spurfowl%" THEN "walking_birds"
    WHEN LOWER(name) LIKE "%lyrebird%" OR LOWER(name) LIKE "%logrunner%" OR LOWER(name) LIKE "%chowchilla%" OR LOWER(name) LIKE "%pitta%" OR LOWER(name) LIKE "%bustard%" OR LOWER(name) LIKE "%pilotbird%" THEN "ground_birds"
    WHEN LOWER(name) LIKE "%catbird%" OR LOWER(name) LIKE "%bower%" THEN "bower"
    WHEN LOWER(name) LIKE "%robin%" OR LOWER(name) LIKE "%redstart%" OR LOWER(name) LIKE "%jay%" OR LOWER(name) LIKE "%bluetail%" OR LOWER(name) LIKE "%minivet%" OR LOWER(name) LIKE "%phoebe%" THEN "robins"
    WHEN LOWER(name) LIKE "%finch%" OR LOWER(name) LIKE "%firetail%" OR LOWER(name) LIKE "%mannikin%" OR LOWER(name) LIKE "%munia%" OR LOWER(name) LIKE "%grosbeak%" OR LOWER(name) LIKE "%towhee%" THEN "finches"
    WHEN LOWER(name) LIKE "%riflebird%" OR LOWER(name) LIKE "%koel%" OR LOWER(name) LIKE "%coucal%" OR LOWER(name) LIKE "%pratincole%" OR LOWER(name) LIKE "%tropicbird%" OR LOWER(name) LIKE "%channel%" OR LOWER(name) LIKE "%friarbird%" THEN "misc"
    WHEN LOWER(name) LIKE "%parrot%" OR LOWER(name) LIKE "%parakeet%" OR LOWER(name) LIKE "%bluebonnet%" OR LOWER(name) LIKE "%lorikeet%" OR LOWER(name) LIKE "%budgerigar%" OR LOWER(name) LIKE "%cockatiel%" OR LOWER(name) LIKE "%ringneck%" THEN "parrots"
    WHEN LOWER(name) LIKE "%cockatoo%" OR LOWER(name) LIKE "%corella%" OR LOWER(name) LIKE "%galah%" THEN "cockatoos"
    WHEN LOWER(name) LIKE "%baza%" OR LOWER(name) LIKE "%shouldered kite%" OR LOWER(name) LIKE "%winged kite%" OR LOWER(name) LIKE "%falcon%" OR LOWER(name) LIKE "%kestrel%" OR LOWER(name) LIKE "%hobby%" OR LOWER(name) LIKE "%merlin%" THEN "small_raptors"
    WHEN LOWER(name) LIKE "%harrier%" OR LOWER(name) LIKE "%eagle%" OR LOWER(name) LIKE "%kite%" OR LOWER(name) LIKE "%hawk%" OR LOWER(name) LIKE "%osprey%" OR LOWER(name) LIKE "%buzzard%" OR LOWER(name) LIKE "%vulture%" THEN "big_raptors"
    WHEN LOWER(name) LIKE "%shag%" OR LOWER(name) LIKE "%darter%" OR LOWER(name) LIKE "%cormorant%" THEN "cormorant"
    WHEN LOWER(name) LIKE "%cuckoo%" THEN "cuckoos"
    WHEN LOWER(name) LIKE "%woodpecker%" OR LOWER(name) LIKE "%flicker%" OR LOWER(name) LIKE "%sapsucker%" THEN "woodpecker"
    WHEN LOWER(name) LIKE "%rosella%" THEN "rosella"
    WHEN LOWER(name) LIKE "%hummingbird%" THEN "hummingbird"
    WHEN LOWER(name) LIKE "%kingfisher%" OR LOWER(name) LIKE "%kookaburra%" THEN "kingfishers"
    WHEN LOWER(name) LIKE "%heron%" OR LOWER(name) LIKE "%bittern%" THEN "herons"
    WHEN LOWER(name) LIKE "%egret%" OR LOWER(name) LIKE "%stork%" OR LOWER(name) LIKE "%spoonbill%" OR LOWER(name) LIKE "%brolga%" OR LOWER(name) LIKE "%crane%" THEN "egrets"
    WHEN LOWER(name) LIKE "%honeyeater%" OR LOWER(name) LIKE "%wattlebird%" OR LOWER(name) LIKE "%miner%" OR LOWER(name) LIKE "%bee-eater%" OR LOWER(name) LIKE "%oriole%" OR LOWER(name) LIKE "%figbird%" THEN "honeyeaters"
    WHEN LOWER(name) LIKE "%chat%" OR LOWER(name) LIKE "%mistletoebird%" OR LOWER(name) LIKE "%bellbird%" OR LOWER(name) LIKE "%monarch%" OR LOWER(name) LIKE "%pardalote%" OR LOWER(name) LIKE "%boatbill%" OR LOWER(name) LIKE "%sunbird%" OR LOWER(name) LIKE "%spinebill%" OR LOWER(name) LIKE "%whiteface%" OR LOWER(name) LIKE "%crossbill%" OR LOWER(name) LIKE "%waxwing%" OR LOWER(name) LIKE "%yellowhammer%"OR LOWER(name) LIKE "%siskin%" OR LOWER(name) LIKE "%firecrest%" OR LOWER(name) LIKE '%goldcrest%' OR LOWER(name) LIKE '%leiothrix%' OR LOWER(name) LIKE '%cardinal%' OR LOWER(name) LIKE '%bluebird%' OR LOWER(name) LIKE '%yellowthroat%' OR LOWER(name) LIKE '%tanager%' THEN "little_colourful_birds"
    WHEN LOWER(name) LIKE "%fairywren%" THEN "fairywren"
    WHEN LOWER(name) LIKE "%penguin%" THEN "penguin"
    WHEN LOWER(name) LIKE "%puffin%" OR LOWER(name) LIKE "%loon%" OR LOWER(name) LIKE "%razorbill%" OR LOWER(name) LIKE "%dovekie%" OR LOWER(name) LIKE "%guillemot%" OR LOWER(name) LIKE "%dovekie%" OR LOWER(name) LIKE "%murre%" OR LOWER(name) LIKE "%auklet%" THEN "puffin_and_co"
    WHEN LOWER(name) LIKE "%stint%" OR LOWER(name) LIKE "%greenshank%" OR LOWER(name) LIKE "%curlew%" OR LOWER(name) LIKE "%whimbrel%" OR LOWER(name) LIKE "%redshank%" OR LOWER(name) LIKE "%knot%" OR LOWER(name) LIKE "%godwit%" OR LOWER(name) LIKE "%dowitcher%" OR LOWER(name) LIKE "%willet%" OR LOWER(name) LIKE "%tattler%" OR LOWER(name) LIKE "%surfbird%" OR LOWER(name) LIKE "%yellowlegs%" THEN "hard_waders"
    WHEN LOWER(name) LIKE "%owl%" OR LOWER(name) LIKE "%nightjar%" OR LOWER(name) LIKE "%whip-poor-will%" OR LOWER(name) LIKE "%nighthawk%"OR LOWER(name) LIKE "%boobook%" OR LOWER(name) LIKE "%frogmouth%" THEN "owl"
    WHEN LOWER(name) LIKE "%stilt%" OR LOWER(name) LIKE "%woodcock%" OR LOWER(name) LIKE "%snipe%" OR LOWER(name) LIKE "%turnstone%"  OR LOWER(name) LIKE "%phalarope%" OR LOWER(name) LIKE "%avocet%" OR LOWER(name) LIKE "%ruff" THEN "colourful_waders"
    WHEN LOWER(name) LIKE "%plover%" OR LOWER(name) LIKE "%sanderling%" OR LOWER(name) LIKE "%dunlin%" OR LOWER(name) LIKE "%lapwing%" OR LOWER(name) LIKE "%oystercatcher%" OR LOWER(name) LIKE "%sandpiper%" OR LOWER(name) LIKE "%dotterel%" OR LOWER(name) LIKE "%killdeer%" THEN "plovers"
    WHEN LOWER(name) LIKE "%rail%" OR LOWER(name) LIKE "%crake%" OR LOWER(name) LIKE "%sora%" THEN "rail_crake"
    WHEN LOWER(name) LIKE "%whistler%" OR LOWER(name) LIKE "%shrike%" OR LOWER(name) LIKE "%wedgebill%" OR LOWER(name) LIKE "%whipbird%" THEN "songbird"
    WHEN LOWER(name) LIKE "%wagtail%" OR LOWER(name) LIKE "%fantail%" OR LOWER(name) LIKE "%flycatcher%" OR LOWER(name) LIKE "%kingbird%" OR LOWER(name) LIKE "%pewee%" THEN "wagfantail"
    WHEN LOWER(name) LIKE '%grackle%' OR LOWER(name) LIKE '%starling%' OR LOWER(name) LIKE '%drongo%' OR LOWER(name) LIKE '%dollarbird%' OR LOWER(name) LIKE '%blackbird%' OR LOWER(name) LIKE '%solitaire%' OR LOWER(name) LIKE '%thrush%' OR LOWER(name) LIKE '%veery%' OR LOWER(name) LIKE '%redwing%' OR LOWER(name) LIKE '%rubythroat%' OR LOWER(name) LIKE '%myna%' OR LOWER(name) LIKE '%ovenbird%' OR LOWER(name) LIKE '%bulbul%' THEN 'ground_mbb'
    WHEN LOWER(name) LIKE "%quail%" OR LOWER(name) LIKE "%grouse%" OR LOWER(name) LIKE "%wanderer%" OR LOWER(name) LIKE "%ptarmigan%" OR LOWER(name) LIKE "%partridge%" OR LOWER(name) LIKE "%chukar%" THEN "quails"
    WHEN LOWER(name) LIKE "%thornbill%" OR LOWER(name) LIKE "%weebill%" OR LOWER(name) LIKE "%scrub-bird%" OR LOWER(name) LIKE "%wren%" OR LOWER(name) LIKE "%treecreeper%" OR LOWER(name) LIKE "%silvereye%" OR LOWER(name) LIKE "%parula%" OR LOWER(name) LIKE "%warbler%" OR LOWER(name) LIKE "%jacky%" OR LOWER(name) LIKE "%sittella%" OR LOWER(name) LIKE "%gerygone%" OR LOWER(name) LIKE "%sparrow%" OR LOWER(name) LIKE "%longspur%" OR LOWER(name) LIKE "%bunting%" OR LOWER(name) LIKE '%redpoll%' OR LOWER(name) LIKE '%bluethroat%' OR LOWER(name) LIKE '%nuthatch%' OR LOWER(name) LIKE '%linnet%' OR LOWER(name) LIKE '%twite%' OR LOWER(name) LIKE '%bobolink%' OR LOWER(name) LIKE '%chiffchaff%' OR LOWER(name) LIKE '%brambling%' OR LOWER(name) LIKE '%blackcap%' OR LOWER(name) LIKE '%eye%' OR LOWER(name) LIKE '%vireo%' OR LOWER(name) LIKE '%kinglet%' THEN "lbb"
    WHEN LOWER(name) LIKE "%cisticola%" OR LOWER(name) LIKE "%babbler%" OR  LOWER(name) LIKE "%lark%" OR LOWER(name) LIKE "%grassbird%" OR LOWER(name) LIKE "%bristlebird%" OR LOWER(name) LIKE "%pipit%" OR LOWER(name) LIKE "%wheatear%" OR LOWER(name) LIKE '%wryneck%' OR LOWER(name) LIKE '%dunnock%' OR LOWER(name) LIKE '%accentor%'  OR LOWER(name) LIKE '%whitethroat%' OR LOWER(name) LIKE '%fieldfare%' OR LOWER(name) LIKE '%dipper%' OR LOWER(name) LIKE "%spinifex%" THEN "mbb"
    WHEN LOWER(name) LIKE "%martin%" OR LOWER(name) LIKE "%swallow%" OR LOWER(name) LIKE "%swift%" THEN "swallows"
    WHEN LOWER(name) LIKE "%tit%" OR LOWER(name) LIKE "%reedling%" OR LOWER(name) LIKE "%chickadee%" THEN "tit"
    WHEN LOWER(name) LIKE "% tern%" OR LOWER(name) LIKE "%skua%" OR LOWER(name) LIKE "%petrel%" OR LOWER(name) LIKE "%prion%" OR LOWER(name) LIKE "%shearwater%" OR LOWER(name) LIKE "%albatross%" OR LOWER(name) LIKE "%gull%" OR LOWER(name) LIKE "%fulmar%" OR LOWER(name) LIKE "%gannet%" OR LOWER(name) LIKE "%noddy%" OR LOWER(name) LIKE "%kittiwake%" OR LOWER(name) LIKE "%booby%" OR LOWER(name) LIKE "%jaeger%" THEN "seabirds"
    WHEN LOWER(name) LIKE "%magpie%" OR LOWER(name) LIKE "%currawong%" OR LOWER(name) LIKE "%butcher%" OR LOWER(name) LIKE "%apostlebird%" OR LOWER(name) LIKE "%chough%" OR LOWER(name) LIKE "%ibis%" OR LOWER(name) LIKE "%jackdaw%" OR LOWER(name) LIKE "%crow%" OR LOWER(name) LIKE "%rook%" OR LOWER(name) LIKE "%raven%" THEN "black_white"
  ELSE NULL
  END AS category
FROM birds
WHERE name NOT LIKE '%sp.%'
