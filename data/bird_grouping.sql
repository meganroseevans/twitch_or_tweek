SELECT
  name,
  image,
  CASE
    WHEN REGEXP_CONTAINS(LOWER(name),r'(quail|pigeon|dove|bronzewing)') THEN 'quails_pigeons'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(duck|teal|hardhead|shoveler|mallard)') THEN 'ducks'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(coot|hen|grebe|pelican)') THEN 'water_birds'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(swan|goose|brushturkey|emu)') THEN 'walking_birds'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(lyrebird|logrunner|chowchilla|pitta|bustard)') THEN 'ground_birds'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(catbird|bower)') THEN 'bower'
    WHEN REGEXP_CONTAINS(LOWER(name),r'robin') THEN 'robins'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(owl|nightjar|boobook|frogmouth)') THEN 'owl'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(finch|firetail|mannikin|munia)') THEN 'finches'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(rifle|koel|coucal|pratincole|tropicbird|channel|friarbird)') THEN 'misc'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(parrot|lorikeet|budgerigar|cockatiel|ringneck)') THEN 'parrots'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(cockatoo|corella|galah)') THEN 'cockatoos'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(baza|eagle|kite|falcon|hawk|kestrel|osprey)') THEN 'raptors'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(darter|cormorant)') THEN 'cormorant'
    WHEN REGEXP_CONTAINS(LOWER(name),r'cuckoo') THEN 'cuckoos'
    WHEN REGEXP_CONTAINS(LOWER(name),r'rosella') THEN 'rosella'
    WHEN REGEXP_CONTAINS(LOWER(name),r'kingfisher') THEN 'kingfisher'
    WHEN REGEXP_CONTAINS(LOWER(name),r'kookaburra') THEN 'kookaburra'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(heron|bittern)') THEN 'herons'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(egret|stork|spoonbill)') THEN 'egrets'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(honeyeater|miner|bee-eater|oriole)') THEN 'honeyeaters'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(chat|mistletoebird|bellbird|monarch|pardalote|pitta|spinifexbird|sunbird|whiteface)') THEN 'little_colourful_birds'
    WHEN REGEXP_CONTAINS(LOWER(name),r'fairywren') THEN 'fairywren'
    WHEN REGEXP_CONTAINS(LOWER(name),r'penguin') THEN 'penguin'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(stilt|stint|rail|turnstone|snipe|plover|lapwing|oystercatcher|sandpiper|dotterel|curlew|avocet)') THEN 'wader'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(rail|crake)') THEN 'rail_crake'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(whistler|shrike|wedgebill|whip)') THEN 'songbird'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(wagtail|fantail|flycatcher)') THEN 'wagfantail'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(magpie|currawong|butcher|apostlebird|chough|ibis)') THEN 'black_white'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(thrush|thornbill|weebill|lark|wren|treecreeper|silvereye|warbler|winter|spinifexbird|cisticola|babbler|grassbird|sittella|bristlebird|pipit|gerygone|pilotbird)') THEN 'lbb'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(martin|swallow|swift)') THEN 'swallows'
    WHEN REGEXP_CONTAINS(LOWER(name),r'(tern|skua|petrel|shearwater|albatross|gull|gannet|noddy)') THEN 'seabirds'
  ELSE NULL
  END AS category
FROM images
