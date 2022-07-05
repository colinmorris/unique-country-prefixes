What is the shortest prefix that uniquely identifies the name of each country? (I'm using "prefix" in [the computer science sense](https://en.wikipedia.org/wiki/Substring#Prefix), so, for example, `S`, `SP`, `SPA`, and `SPAI` are all prefixes of `SPAIN`, as well as `SPAIN` itself, and the empty string, ε.)

An alternative formulation: if you had an autocomplete field for choosing a country, what is the shortest sequence of letters you would have to type before your options are narrowed down to one specific country?

Example: `SWE` is the shortest unique prefix for Sweden. Sweden is the only country that begins with this letter sequence, and there is no shorter prefix that has this property (because, for example, `SW` is shared with Switzerland).

Some possibly surprising facts:

- There are 3 countries that are uniquely specified by their first letter
- The 2 countries with the longest shortest unique prefixes require 13 characters (including spaces) to distinguish: `REPUBLIC OF _`
- There are 2 countries whose shortest unique prefix is not "proper" - i.e. it is the whole name of the country. (3 if you count Iran - see information on data sources below.)
- There are 3 countries that have *no* unique prefix!

## Data

For the purposes of this experiment, I used the 192 United Nations member states as of July 2022. I used the English name listed on the UN website [here](https://www.un.org/en/about-us/member-states), which may differ from the country's endonym or official full English name (e.g. 'Germany', rather than 'Deutschland' or 'Federal Republic of Germany'). Most of the forms used here are the recognizable ones used in everyday conversation, though there are a few exceptions (e.g. the country commonly known as Turkey has requested to be referred to as Türkiye as of May 2022).

I used the repository [cristiroma/countries](https://github.com/cristiroma/countries) for two purposes:
- For the flag icons used in the generated infographics. To load these images locally, you'll need to clone the countries repo under the root of this repo.
- To generate countries.csv. I started from the file at countries/data/csv/countries.csv, then manually winnowed it down to just the UN member states, and manually updated the first 'name' column for a couple states to match the form currently used by the UN.

## Infographic generation

The IPython notebook prefixes.ipynb generates an html file `pres.html`.

I then convert this into a pdf using Chrome's 'print to pdf' feature, using the minimal margin setting.

Then I convert *that* to an image using the following Imagemagick invocation:

```bash
convert -density 150 -trim pres.pdf -quality 100 pres.jpg
```

(Grossly circuitous, I know.)

The notebook also generates another html file, `spoilers.html`, which is identical except that it includes the css file `sstyles.css` rather than `styles.css`. This differs in that it shows the full name of each entry, rather than just a flag and prefix.
