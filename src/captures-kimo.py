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
    ('ki-10-anglais.png', 'en/franchise.html', '#parcours', None, 'en'),
    # La page du concept, celle qui porte sa note.
    ('ki-12-concept.png', 'concept.html', None, None, 'fr'),
    ('ki-13-couches.png', 'concept.html', '#couches', None, 'fr'),
    ('ki-14-format.png', 'concept.html', '#format', None, 'fr'),
    ('ki-15-piliers.png', 'concept.html', '#apprentissage', None, 'fr'),
    ('ki-16-journee.png', 'concept.html', '#journee', None, 'fr'),
    ('ki-17-exploitation.png', 'concept.html', '#exploitation', None, 'fr'),
    ('ki-18-phases.png', 'concept.html', '#phases', None, 'fr'),
    ('ki-19-concept-anglais.png', 'en/concept.html', '#apprentissage',
     None, 'en'),
    # KIMO Tutoring, et la version anglaise qui a maintenant sa propre
    # adresse : on la capture sur SON fichier, pas apres un clic.
    ('ki-21-tutorat.png', 'tutoring.html', None, None, 'fr'),
    ('ki-22-tutorat-programmes.png', 'tutoring.html', '#programmes', None,
     'fr'),
    ('ki-23-tutorat-securite.png', 'tutoring.html', '#securite', None, 'fr'),
    ('ki-24-tutorat-mvp.png', 'tutoring.html', '#mvp', None, 'fr'),
    ('ki-25-anglais-accueil.png', 'en/index.html', None, None, 'en'),
    ('ki-26-anglais-tutorat.png', 'en/tutoring.html', '#programmes', None,
     'en'),
    ('ki-27-anglais-concept.png', 'en/concept.html', '#journee', None, 'en'),
]


def main():
    with sync_playwright() as pw:
        nav = pw.chromium.launch()
        ctx = nav.new_context(viewport={'width': 1280, 'height': 800},
                              device_scale_factor=1)
        page = ctx.new_page()
        for nom, fichier, ancre, _x, langue in VUES:
            page.goto(url(fichier))
            # Plus de clic de bascule : la langue est celle de l'ADRESSE.
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
        page.goto(url('tutoring.html'))
        page.evaluate(
            "() => { const n = document.querySelector('#programmes');"
            " window.scrollTo(0, n.getBoundingClientRect().top"
            " + window.scrollY - 12); }")
        page.wait_for_timeout(150)
        page.screenshot(path=os.path.join(ICI, 'ki-20-mobile-tutorat.png'))
        print('ki-20-mobile-tutorat.png')
        ctx.close()
        nav.close()


if __name__ == '__main__':
    main()
