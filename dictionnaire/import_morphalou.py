"""Turns Morphalou 3.1 into dict/morphalou.txt: the words it adds to
Grammalecte's for a board game, those of its lexicographers' own part.
Usage: python dict/import_morphalou.py <Morphalou3.1_formatCSV_toutEnUn.zip or .csv>
Morphalou 3.1 (ATILF, CNRS) is on ORTOLANG, under the LGPL-LR:
https://repository.ortolang.fr/api/content/morphalou/latest/

Morphalou merges five lexicons; each inflected form says which ones hold it.
Only the forms of Morphalou 2 are kept - checked by ATILF's lexicographers,
where DELA and Lefff, generated, bring hundreds of thousands of doubtful
conjugations and abbreviations filed as nouns. Kept too: common nouns,
adjectives, verbs, adverbs, interjections and the small words; left out:
set phrases, forms with a capital letter, and words without a vowel ("cd",
"kg"). Accents, hyphens and apostrophes are dropped later, when the
dictionary is built (mots::normalizeWord), as Grammalecte's are.
"""
import io
import pathlib
import sys
import unicodedata
import zipfile

KEPT = {"Nom commun", "Adjectif qualificatif", "Verbe", "Adverbe", "Interjection",
        "Préposition", "Conjonction", "Pronom", "Déterminant", "Nombre"}
VOWELS = set("aeiouy")


def csv_lines(path):
    if path.suffix == ".zip":
        with zipfile.ZipFile(path) as archive:
            name = next(n for n in archive.namelist() if n.endswith(".csv"))
            with archive.open(name) as raw:
                yield from io.TextIOWrapper(raw, encoding="utf-8")
    else:
        with open(path, encoding="utf-8") as file:
            yield from file


def plain(word):
    """Without accents nor ligatures, for the vowel check."""
    word = word.replace("œ", "oe").replace("æ", "ae")
    return "".join(c for c in unicodedata.normalize("NFD", word) if not unicodedata.combining(c))


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    words = set()
    category = locution = ""
    for line in csv_lines(pathlib.Path(sys.argv[1])):
        fields = line.rstrip("\n").split(";")
        if len(fields) < 18 or fields[0] in ("GRAPHIE", "LEMME"):
            continue  # the notice, the column titles
        if fields[0]:  # a new lemma; its forms follow, the lemma's columns empty
            category, locution = fields[2], fields[4]
        form, sources = fields[9], fields[17].split()
        if not form or category not in KEPT or locution or " " in form:
            continue
        if "morphalou2" not in sources or any(c.isupper() for c in form):
            continue
        if not VOWELS & set(plain(form)):
            continue
        words.add(form)
    out = pathlib.Path(__file__).with_name("morphalou.txt")
    with open(out, "w", encoding="utf-8", newline="\n") as file:
        file.write("# Formes fléchies de Morphalou 3.1 (ATILF, CNRS), sa part Morphalou 2 :\n")
        file.write("# https://repository.ortolang.fr/api/content/morphalou/latest/\n")
        file.write("# Licence LGPL-LR : voir LICENCE-morphalou.txt. Produit par\n")
        file.write("# dict/import_morphalou.py : ne pas modifier à la main.\n")
        for word in sorted(words):
            file.write(word + "\n")
    print(f"{out}: {len(words)} formes")


if __name__ == "__main__":
    main()
