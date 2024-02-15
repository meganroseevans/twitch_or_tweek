/* A script for retrieving bird names and images from eBird

- For Photos, go to  https://media.ebird.org/catalog?regionCode=AU&sort=rating_rank_desc&mediaType=photo
- For Audio, go to  https://media.ebird.org/catalog?regionCode=AU&sort=rating_rank_desc&mediaType=audio
- Click 'More Results' a bunch of times
- Inspect page, go to Console, run the below code
- Save output by right clicking on object, copy and paste into new file called 'get_bird_images_output.json'
- To convert it from a json to csv, run `$ jq -r '.[] | [.name, .image_id] | @csv' get_bird_images_output.json > get_bird_images_output.csv
- To add these new images to the existing image database, run `$ cat images.csv <(echo) get_bird_images_output.csv > images.csv`
- To remove duplicates, run `$ sort -u images.csv -o images.csv`
*/

function collectMatchingImageAttributes() {
  const prefix = 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/';
  const images = document.querySelectorAll('img');

  const matchingImages = Array.from(images).filter((img) => img.src.startsWith(prefix)).map((fimg) => {
    const alt = fimg.alt.split(' - ')[0].trim();
    const cc = fimg.alt.split(' - ')[1].trim();
    const srcParts = fimg.src.split('/');
    const src = srcParts[srcParts.length - 2];

    return { alt, cc, src };
  });

  return matchingImages;
}

const matchingImageAttributes = collectMatchingImageAttributes();
console.log(matchingImageAttributes);
