# -*- coding: utf-8 -*-
"""Captures d'ecran du site KIMO, pour relecture par le client.

Jamais full_page : une page longue produit une image de plusieurs milliers
de pixels de haut. On se place sur la section voulue et on prend la fenetre.
"""

import os
from playwright.sync_api import sync_playwright

from chemins import dossier_pages

ICI = os.path.dirname(os.path.abspath(__file__))
DEMO = dossier_pages(ICI)


def url(nom):
    return 'file://' + os.path.join(DEMO, nom)


VUES = [
    ('ki-1-accueil.png', 'index.html', None, None, 'fr'),
    ('ki-2-modele.png', 'index.html', '#modele', None, 'fr'),
    ('ki-3-methode.png', 'index.html', '#methode', None, 'fr'),
    ('ki-4-reglementaire.png', 'index.html', '#cadre', None, 'fr'),
    ('ki-5-franchise.png', 'franchise.html', None, None, 'fr'),
    ('ki-6-parcours.png', 'franchise.html', '#parcours', None, 'fr'),
    ('ki-7-modele-eco.png', 'franchise.html', '#modele-eco', None, 'fr'),
    ('ki-8-simulateur.png', 'franchise.html', '#simulateur', None, 'fr'),
    ('ki-9-candidature.png', 'franchise.html', '#candidature', None, 'fr'),
    ('ki-10-anglais.png', 'franchise.html', '#parcours', None, 'en'),
]


def main():
    with sync_playwright() as pw:
        nav = pw.chromium.launch()
        ctx = nav.new_context(viewport={'width': 1280, 'height': 800},
                              device_scale_factor=1)
        page = ctx.new_page()
        for nom, fichier, ancre, _x, langue in VUES:
            page.goto(url(fichier))
            if langue == 'en':
                page.click('.langue button[data-l="en"]')
            else:
                page.click('.langue button[data-l="fr"]')
            if ancre:
                page.evaluate(
                    "s => { const n = document.querySelector(s);"
                    " window.scrollTo(0, n.getBoundingClientRect().top"
                    " + window.scrollY - 70); }", ancre)
            page.wait_for_timeout(180)
            page.screenshot(path=os.path.join(ICI, nom))
            print(nom)
        ctx.close()

        # Mobile — un seul cliche, la largeur qui compte.
        ctx = nav.new_context(viewport={'width': 390, 'height': 800})
        page = ctx.new_page()
        page.goto(url('index.html'))
        page.wait_for_timeout(150)
        page.screenshot(path=os.path.join(ICI, 'ki-11-mobile.png'))
        print('ki-11-mobile.png')
        ctx.close()
        nav.close()


if __name__ == '__main__':
    main()
