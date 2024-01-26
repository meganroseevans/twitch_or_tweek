SELECT
  name,
  image_id,
  CASE
    WHEN REGEXP_CONTAINS(LOWER(name),"(quail|pigeon|dove|bronzewing)") THEN "quails_pigeons"
    WHEN REGEXP_CONTAINS(LOWER(name),"(duck|teal|hardhead|shoveler|mallard)") THEN "ducks"
    WHEN REGEXP_CONTAINS(LOWER(name),"(coot|hen|grebe|pelican)") THEN "water_birds"
    WHEN REGEXP_CONTAINS(LOWER(name),"(swan|goose|brushturkey|emu)") THEN "walking_birds"
    WHEN REGEXP_CONTAINS(LOWER(name),"(lyrebird|logrunner|chowchilla|pitta|bustard)") THEN "ground_birds"
    WHEN REGEXP_CONTAINS(LOWER(name),"(catbird|bower)") THEN "bower"
    WHEN REGEXP_CONTAINS(LOWER(name),"robin") THEN "robins"
    WHEN REGEXP_CONTAINS(LOWER(name),"(owl|nightjar|boobook|frogmouth)") THEN "owl"
    WHEN REGEXP_CONTAINS(LOWER(name),"(finch|firetail|mannikin|munia)") THEN "finches"
    WHEN REGEXP_CONTAINS(LOWER(name),"(rifle|koel|coucal|pratincole|tropicbird|channel|friarbird)") THEN "misc"
    WHEN REGEXP_CONTAINS(LOWER(name),"(parrot|lorikeet|budgerigar|cockatiel|ringneck)") THEN "parrots"
    WHEN REGEXP_CONTAINS(LOWER(name),"(cockatoo|corella|galah)") THEN "cockatoos"
    WHEN REGEXP_CONTAINS(LOWER(name),"(baza|eagle|kite|falcon|hawk|kestrel|osprey)") THEN "raptors"
    WHEN REGEXP_CONTAINS(LOWER(name),"(darter|cormorant)") THEN "cormorant"
    WHEN REGEXP_CONTAINS(LOWER(name),"cuckoo") THEN "cuckoos"
    WHEN REGEXP_CONTAINS(LOWER(name),"rosella") THEN "rosella"
    WHEN REGEXP_CONTAINS(LOWER(name),"kingfisher") THEN "kingfisher"
    WHEN REGEXP_CONTAINS(LOWER(name),"kookaburra") THEN "kookaburra"
    WHEN REGEXP_CONTAINS(LOWER(name),"(heron|bittern)") THEN "herons"
    WHEN REGEXP_CONTAINS(LOWER(name),"(egret|stork|spoonbill)") THEN "egrets"
    WHEN REGEXP_CONTAINS(LOWER(name),"(honeyeater|miner|bee-eater|oriole)") THEN "honeyeaters"
    WHEN REGEXP_CONTAINS(LOWER(name),"(chat|mistletoebird|bellbird|monarch|pardalote|pitta|spinifexbird|sunbird|whiteface)") THEN "little_colourful_birds"
    WHEN REGEXP_CONTAINS(LOWER(name),"fairywren") THEN "fairywren"
    WHEN REGEXP_CONTAINS(LOWER(name),"penguin") THEN "penguin"
    WHEN REGEXP_CONTAINS(LOWER(name),"(stilt|stint|rail|turnstone|snipe|plover|lapwing|oystercatcher|sandpiper|dotterel|curlew|avocet)") THEN "wader"
    WHEN REGEXP_CONTAINS(LOWER(name),"(rail|crake)") THEN "rail_crake"
    WHEN REGEXP_CONTAINS(LOWER(name),"(whistler|shrike|wedgebill|whip)") THEN "songbird"
    WHEN REGEXP_CONTAINS(LOWER(name),"(wagtail|fantail|flycatcher)") THEN "wagfantail"
    WHEN REGEXP_CONTAINS(LOWER(name),"(magpie|currawong|butcher|apostlebird|chough|ibis)") THEN "black_white"
    WHEN REGEXP_CONTAINS(LOWER(name),"(thrush|thornbill|weebill|lark|wren|treecreeper|silvereye|warbler|winter|spinifexbird|cisticola|babbler|grassbird|sittella|bristlebird|pipit|gerygone|pilotbird)") THEN "lbb"
    WHEN REGEXP_CONTAINS(LOWER(name),"(martin|swallow|swift)") THEN "swallows"
    WHEN REGEXP_CONTAINS(LOWER(name),"(tern|skua|petrel|shearwater|albatross|gull|gannet|noddy)") THEN "seabirds"
  ELSE NULL
  END AS category
FROM birds
