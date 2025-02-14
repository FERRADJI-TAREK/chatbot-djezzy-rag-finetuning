import scrapy
import re
from w3lib.html import remove_tags  

class DjezzyscrapeSpider(scrapy.Spider):
    name = "djezzyscrape1"
    allowed_domains = ["www.djezzy.dz"]
    
    
    start_urls = [
        "https://www.djezzy.dz/particuliers/offres/offres-internet/",
        "https://www.djezzy.dz/particuliers/offres/djezzy-hayla-maxi/",
        "https://www.djezzy.dz/particuliers/offres/djezzy-confort-2/",
        "https://www.djezzy.dz/particuliers/offres/djezzy-hayla-bezzef/"
    ]

    def parse(self, response):
        offres = response.css('div.col-centered.col-xs-12.col-sm-4')
        
        for offre in offres:
            internet = offre.css('th').get()
            autre_benefice = offre.css('tbody').get()
            
            
            internet_clean = remove_tags(internet).strip() if internet else "Non spécifié"
            autre_benefice_clean = remove_tags(autre_benefice).strip() if autre_benefice else "Non spécifié"

            # Deduce the offer name from the URL.
            nom_offre = response.url.split("/")[-2].replace("-", " ").title()

            yield {
                'Nom de l\'offre': nom_offre,
                'Internet': internet_clean,
                'Autres bénéfices': autre_benefice_clean
            }
