#!/usr/bin/env python
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a set of bibtex of publications and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). 
# 
# The core python code is also in `pubsFromBibs.py`. 
# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
# 
# TODO: Make this work with other databases of citations, 
# TODO: Merge this with the existing TSV parsing solution


from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re

#todo: incorporate different collection types rather than a catch all publications, requires other changes to template
publist = {
    @article{kilimnik2012quantification,
  title={Quantification of islet size and architecture},
  author={Kilimnik, German and Jo, Junghyo and Periwal, Vipul and Zielinski, Mark C and Hara, Manami},
  journal={Islets},
  volume={4},
  number={2},
  pages={167--172},
  year={2012},
  publisher={Taylor \& Francis}
}

@article{wang2013regional,
  title={Regional differences in islet distribution in the human pancreas-preferential beta-cell loss in the head region in patients with type 2 diabetes},
  author={Wang, Xiaojun and Misawa, Ryosuke and Zielinski, Mark C and Cowen, Peter and Jo, Junghyo and Periwal, Vipul and Ricordi, Camillo and Khan, Aisha and Szust, Joel and Shen, Junhui and others},
  journal={PloS one},
  volume={8},
  number={6},
  pages={e67454},
  year={2013},
  publisher={Public Library of Science}
}

@article{wang2013quantitative,
  title={Quantitative analysis of pancreatic polypeptide cell distribution in the human pancreas},
  author={Wang, Xiaojun and Zielinski, Mark C and Misawa, Ryosuke and Wen, Patrick and Wang, Tian-Yuan and Wang, Cheng-Zhang and Witkowski, Piotr and Hara, Manami},
  journal={PloS one},
  volume={8},
  number={1},
  pages={e55501},
  year={2013},
  publisher={Public Library of Science}
}

@article{manfredi2012effect,
  title={The effect of surface wave propagation on neural responses to vibration in primate glabrous skin},
  author={Manfredi, Louise R and Baker, Andrew T and Elias, Damian O and Dammann III, John F and Zielinski, Mark C and Polashock, Vicky S and Bensmaia, Sliman J},
  journal={PloS one},
  volume={7},
  number={2},
  pages={e31203},
  year={2012},
  publisher={Public Library of Science}
}

@article{manfredi2014natural,
  title={Natural scenes in tactile texture},
  author={Manfredi, Louise R and Saal, Hannes P and Brown, Kyler J and Zielinski, Mark C and Dammann III, John F and Polashock, Vicky S and Bensmaia, Sliman J},
  journal={Journal of neurophysiology},
  volume={111},
  number={9},
  pages={1792--1802},
  year={2014},
  publisher={American Physiological Society Bethesda, MD}
}

@article{savari2013distinct,
  title={Distinct function of the head region of human pancreas in the pathogenesis of diabetes},
  author={Savari, Omid and Zielinski, Mark C and Wang, Xiaojun and Misawa, Ryosuke and Millis, J Michael and Witkowski, Piotr and Hara, Manami},
  journal={Islets},
  volume={5},
  number={5},
  pages={226--228},
  year={2013},
  publisher={Taylor \& Francis}
}

@article{bailey2014evidence,
  title={Evidence of non-pancreatic beta cell-dependent roles of Tcf7l2 in the regulation of glucose metabolism in mice},
  author={Bailey, Kathleen A and Savic, Daniel and Zielinski, Mark and Park, Soo-Young and Wang, Ling-jia and Witkowski, Piotr and Brady, Matthew and Hara, Manami and Bell, Graeme I and Nobrega, Marcelo A},
  journal={Human molecular genetics},
  volume={24},
  number={6},
  pages={1646--1654},
  year={2014},
  publisher={Oxford University Press}
}

@article{golab2013optimization,
  title={optimization of the Coating of Pancreatic Islets with T Regulatory Cells in the Novel Immunoprotective Approach.: abstract\# A694},
  author={Golab, K and Kizilel, S and Bal, T and Hara, M and Zielinski, M and Wang, X and Grzanka, J and Wang, L and Cochet, O and Tibudan, M and others},
  journal={American Journal of Transplantation},
  volume={13},
  pages={242},
  year={2013},
  publisher={American Journal of Transplantation}
}

@inproceedings{golab2013biotin,
  title={Biotin-PEG-SVA as a more Effective Linking Molecule in Comparison to Biotin-PEG-NHS for Coating of Pancreatic Islets with Regulatory T Cells (Tregs) to Create Local Immunoprotection-Optimization of the Method},
  author={Golab, Karolina and Kizilel, Seda and Bal, Tugba and Hara, Manami and Zielinski, Mark and Wang, Xiao-Jun and Grzanka, Jakub and Wang, Ling-Jia and Cochet, Olivia and Tibudan, Martin and others},
  booktitle={TRANSPLANTATION},
  volume={96},
  number={6},
  pages={S63--S63},
  year={2013},
  organization={LIPPINCOTT WILLIAMS \& WILKINS 530 WALNUT ST, PHILADELPHIA, PA 19106-3621 USA}
}

@inproceedings{golkab2014improved,
  title={Improved Coating of Pancreatic Islets With Regulatory T cells to Create Local Immunosuppression by Using the Biotin-polyethylene Glycol-succinimidyl Valeric Acid Ester Molecule},
  author={Go{\l}{\k{a}}b, K and Kizilel, S and Bal, T and Hara, M and Zielinski, M and Grose, R and Savari, O and Wang, X-J and Wang, L-J and Tibudan, M and others},
  booktitle={Transplantation proceedings},
  volume={46},
  number={6},
  pages={1967--1971},
  year={2014},
  organization={Elsevier}
}

@inproceedings{zielinski2013histological,
  title={Histological Analysis of the Whole Human Pancreas in Health and Disease},
  author={Zielinski, Mark C and Wang, Xiaojun and Misawa, Ryosuke and Wang, Ling-Jia and Witkowski, Piotr and Hara, Manami},
  booktitle={DIABETES},
  volume={62},
  pages={A563--A563},
  year={2013},
  organization={AMER DIABETES ASSOC 1701 N BEAUREGARD ST, ALEXANDRIA, VA 22311-1717 USA}
}

@inproceedings{greeley2013fewer,
  title={Fewer Beta Cells and Insulin Granules in Autopsy Histology of a Patient With Sulfonylurea-Unresponsive KCNJ11 Neonatal Diabetes},
  author={Greeley, Siri Atma W and Zielinski, Mark C and Wood, Jamie R and Steiner, Donald F and Bell, Graeme I and Philipson, Louis H and Hara, Manami},
  booktitle={DIABETES},
  volume={62},
  pages={A562--A562},
  year={2013},
  organization={AMER DIABETES ASSOC 1701 N BEAUREGARD ST, ALEXANDRIA, VA 22311-1717 USA}
}

@article{poudel2016stereological,
  title={Stereological analyses of the whole human pancreas},
  author={Poudel, Ananta and Fowler, Jonas L and Zielinski, Mark C and Kilimnik, German and Hara, Manami},
  journal={Scientific reports},
  volume={6},
  pages={34049},
  year={2016},
  publisher={Nature Publishing Group}
}

@article{greeley2016preservation,
  title={Preservation of Reduced Numbers of Insulin-Positive Cells in Sulfonylurea-Unresponsive KCNJ11-Related Diabetes},
  author={Greeley, Siri Atma W and Zielinski, Mark C and Poudel, Ananta and Ye, Honggang and Berry, Shivani and Taxy, Jerome B and Carmody, David and Steiner, Donald F and Philipson, Louis H and Wood, Jamie R and others},
  journal={The Journal of Clinical Endocrinology \& Metabolism},
  volume={102},
  number={1},
  pages={1--5},
  year={2016},
  publisher={Endocrine Society Washington, DC}
}

@article{papale2016interplay,
  title={Interplay between Hippocampal Sharp-Wave-Ripple Events and Vicarious Trial and Error Behaviors in Decision Making},
  author={Papale, Andrew E and Zielinski, Mark C and Frank, Loren M and Jadhav, Shantanu P and Redish, A David},
  journal={Neuron},
  volume={92},
  number={5},
  pages={975--982},
  year={2016},
  publisher={Elsevier}
}

@article{zielinski2017role,
  title={The role of replay and theta sequences in mediating hippocampal-prefrontal interactions for memory and cognition},
  author={Zielinski, Mark C and Tang, Wenbo and Jadhav, Shantanu P},
  journal={Hippocampus},
  year={2017},
  publisher={Wiley Online Library}
}
}

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


for pubsource in publist:
    parser = bibtex.Parser()
    bibdata = parser.parse_file(publist[pubsource]["file"])

    #loop through the individual references in a given bibtex file
    for bib_id in bibdata.entries:
        #reset default date
        pub_year = "1900"
        pub_month = "01"
        pub_day = "01"
        
        b = bibdata.entries[bib_id].fields
        
        try:
            pub_year = f'{b["year"]}'

            #todo: this hack for month and day needs some cleanup
            if "month" in b.keys(): 
                if(len(b["month"])<3):
                    pub_month = "0"+b["month"]
                    pub_month = pub_month[-2:]
                elif(b["month"] not in range(12)):
                    tmnth = strptime(b["month"][:3],'%b').tm_mon   
                    pub_month = "{:02d}".format(tmnth) 
                else:
                    pub_month = str(b["month"])
            if "day" in b.keys(): 
                pub_day = str(b["day"])

                
            pub_date = pub_year+"-"+pub_month+"-"+pub_day
            
            #strip out {} as needed (some bibtex entries that maintain formatting)
            clean_title = b["title"].replace("{", "").replace("}","").replace("\\","").replace(" ","-")    

            url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
            url_slug = url_slug.replace("--","-")

            md_filename = (str(pub_date) + "-" + url_slug + ".md").replace("--","-")
            html_filename = (str(pub_date) + "-" + url_slug).replace("--","-")

            #Build Citation from text
            citation = ""

            #citation authors - todo - add highlighting for primary author?
            for author in bibdata.entries[bib_id].persons["author"]:
                citation = citation+" "+author.first_names[0]+" "+author.last_names[0]+", "

            #citation title
            citation = citation + "\"" + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + ".\""

            #add venue logic depending on citation type
            venue = publist[pubsource]["venue-pretext"]+b[publist[pubsource]["venuekey"]].replace("{", "").replace("}","").replace("\\","")

            citation = citation + " " + html_escape(venue)
            citation = citation + ", " + pub_year + "."

            
            ## YAML variables
            md = "---\ntitle: \""   + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + '"\n'
            
            md += """collection: """ +  publist[pubsource]["collection"]["name"]

            md += """\npermalink: """ + publist[pubsource]["collection"]["permalink"]  + html_filename
            
            note = False
            if "note" in b.keys():
                if len(str(b["note"])) > 5:
                    md += "\nexcerpt: '" + html_escape(b["note"]) + "'"
                    note = True

            md += "\ndate: " + str(pub_date) 

            md += "\nvenue: '" + html_escape(venue) + "'"
            
            url = False
            if "url" in b.keys():
                if len(str(b["url"])) > 5:
                    md += "\npaperurl: '" + b["url"] + "'"
                    url = True

            md += "\ncitation: '" + html_escape(citation) + "'"

            md += "\n---"

            
            ## Markdown description for individual page
            if note:
                md += "\n" + html_escape(b["note"]) + "\n"

            if url:
                md += "\n[Access paper here](" + b["url"] + "){:target=\"_blank\"}\n" 
            else:
                md += "\nUse [Google Scholar](https://scholar.google.com/scholar?q="+html.escape(clean_title.replace("-","+"))+"){:target=\"_blank\"} for full citation"

            md_filename = os.path.basename(md_filename)

            with open("../_publications/" + md_filename, 'w') as f:
                f.write(md)
            print(f'SUCESSFULLY PARSED {bib_id}: \"', b["title"][:60],"..."*(len(b['title'])>60),"\"")
        # field may not exist for a reference
        except KeyError as e:
            print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', b["title"][:30],"..."*(len(b['title'])>30),"\"")
            continue
