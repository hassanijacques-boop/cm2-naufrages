#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cahier journal Lundi 24 août 2026 - version détaillée avec charte de classe."""
from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_fill_color(15, 23, 42)
        self.rect(0, 0, 210, 7, 'F')
        self.set_xy(10, 10)
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(15, 23, 42)
        self.cell(0, 7, 'RENTREE SCOLAIRE 2026-2027 - ECOLE LA ROSE', align='C')
        self.ln(7)
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 6, 'CAHIER JOURNAL - Lundi 24 août 2026 - 7h00 a 12h00', align='C')
        self.ln(6)
        self.set_font('Helvetica', '', 10)
        self.set_text_color(80, 80, 90)
        self.cell(0, 5, 'Classe CM1/CM2 - M. Hassani Moustoifa - Bandraboua', align='C')
        self.ln(2)
        self.set_draw_color(245, 158, 11)
        self.set_line_width(0.7)
        self.line(10, self.get_y()+2, 200, self.get_y()+2)
        self.ln(6)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(150, 150, 160)
        self.cell(0, 5, 'Cahier journal - Lundi 24 août 2026 - page ' + str(self.page_no()), align='C')

    def section(self, title):
        self.ln(2)
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(245, 158, 11)
        self.cell(0, 6, title, ln=True)
        self.ln(1)

    def bullet(self, txt, indent=0):
        self.set_font('Helvetica', '', 9.5)
        self.set_text_color(30, 41, 59)
        x = self.l_margin + indent
        self.set_x(x)
        width = self.w - self.r_margin - x
        self.multi_cell(width, 4.8, txt)
        self.ln(0.5)

def main():
    pdf = PDF('P', 'mm', 'A4')
    pdf.add_page()

    # ===== OBJECTIFS =====
    pdf.section('OBJECTIFS DE LA JOURNEE')
    pdf.bullet('- Vivre ensemble : accueillir les élèves, creer un climat de confiance, connaitre les prenoms, poser les regles de vie.')
    pdf.bullet('- Francais : evaluer le niveau de depart en lecture/comprehension et orthographe.')
    pdf.bullet('- Mathematiques : evaluer le niveau de depart en numeration/calcul et problemes.')
    pdf.bullet('- Competences transversales : ecouter les autres, prendre la parole en groupe, respecter les regles, s\'investir dans son travail.')
    pdf.ln(2)

    # ===== DEROULE DETAILLE =====
    pdf.section('DEROULE DE LA MATINEE - chaque creneau detaille')

    rows = [
        ('7h00-7h20', '20 min', 'Accueil',
         '1. Etre devant la porte des 7h00, accueillir chaque eleve avec un sourire et son prenom.\n'
         '2. Guider chaque eleve vers sa place (etiquette prenom sur la table).\n'
         '3. Verifier le materiel (trousse, cahiers) et noter les manques.\n'
         '4. Les eleves installes dessinent librement ou lisent un album pose sur la table.'),
        ('7h20-7h35', '15 min', 'Vivre ensemble - Mot de bienvenue',
         '1. Se presenter : nom, prenom, annonce de la classe (CM1/CM2).\n'
         '2. Presenter la journee : "Aujourd\'hui, on apprend a se connaitre et je verifie ce que vous savez deja."\n'
         '3. Annoncer les grandes lignes de l\'annee : le projet "Les Naufrages de l\'ilot perdu", les sorties.\n'
         '4. Repondre aux questions des eleves (5 min max).'),
        ('7h35-8h05', '30 min', 'Vivre ensemble - Jeu 1 : La roue des prenoms',
         '1. Faire asseoir les eleves en cercle (par terre ou chaises).\n'
         '2. L\'enseignant commence : "Je m\'appelle M. Hassani et j\'aime le football."\n'
         '3. Chaque eleve repete les prenoms deja dits puis donne le sien + un gout.\n'
         '4. Le dernier recite tous les prenoms de la classe.\n'
         '5. Regle : la classe aide en chuchotant si un eleve oublie. Pas de moquerie.\n'
         '6. Observer : qui parle fort, qui est timide, quels prenoms difficiles (noter).'),
        ('8h05-8h35', '30 min', 'Vivre ensemble - Jeu 2 : Les 3 verites',
         '1. Distribuer une feuille + un crayon a chaque eleve.\n'
         '2. Expliquer : chacun ecrit 3 phrases sur lui (2 vraies, 1 fausse).\n'
         '3. Donner son exemple au tableau (avec humour).\n'
         '4. Les eleves ecrivent (10 min - aider ceux en difficulte).\n'
         '5. Chaque eleve lit ses phrases, la classe devine la fausse.\n'
         '6. Observer : ecriture, langage oral, personnalite (noter discretement).'),
        ('8h35-9h05', '30 min', 'Vivre ensemble - LA CHARTE DE CLASSE',
         '1. Question de depart (5 min) : "Pourquoi une classe a-t-elle besoin de regles ?" - recueillir 5-6 idees au tableau.\n'
         '2. Echanges (10 min) : "Qu\'est-ce qui nous empeche de travailler ?" (bruit, moqueries, violence...) puis "Quelles regles pour eviter ca ?" - les eleves proposent, l\'enseignant reformule en positif.\n'
         '3. Synthese (10 min) : afficher les 5 regles au tableau (Respect, Ecoute, Parole, Travail, Securite) - les lire ensemble, expliquer chaque regle avec un exemple concret ("Respect = on ne se moque pas, comme dans le jeu des prenoms").\n'
         '4. Consequences (5 min) : expliquer le systeme en 3 temps (1er regard + rappel, 2e deplacement + discussion, 3e reflexion ecrite + info parents).\n'
         '5. Chaque eleve recopie la charte dans son cahier de vie (ou la colle) et la signe. Afficher la charte grand format au mur.'),
        ('9h05-9h25', '20 min', 'Recreation',
         'Surveillance de la cour : etre visible, circuler, surveiller les coins, verifier les retours.'),
        ('9h25-9h55', '30 min', 'Francais - Evaluation diagnostique 1 : lecture',
         '1. Consigne : "Ce n\'est pas une note. C\'est pour que je sache ce que vous savez deja."\n'
         '2. Distribuer le texte (~8 lignes : Amina et Rachid au lagon).\n'
         '3. Lecture silencieuse (5 min) puis les 6 questions (comprehension).\n'
         '4. Pendant ce temps : appeler les eleves 1 par 1 pour la lecture a voix haute (1 min chacun) - noter la fluidite sur la grille.\n'
         '5. Ramasser les feuilles.'),
        ('9h55-10h25', '30 min', 'Francais - Evaluation diagnostique 2 : orthographe',
         '1. Exercice 1 : recopier 5 phrases sans erreur.\n'
         '2. Exercice 2 : souligner le verbe, entourer le sujet (3 phrases).\n'
         '3. Exercice 3 : accorder le verbe (3 phrases).\n'
         '4. Lire chaque consigne a voix haute, faire un exemple au tableau.\n'
         '5. Observer : orthographe lexicale, accords, classes de mots (grille).'),
        ('10h25-10h55', '30 min', 'Maths - Evaluation diagnostique 3 : numeration/calcul',
         '1. Exercice 1 : ecrire en chiffres (3 nombres jusqu\'a 10 000).\n'
         '2. Exercice 2 : decomposer (2 nombres).\n'
         '3. Exercice 3 : calculer (4 operations : +, -, x, /).\n'
         '4. Lire les consignes, exemple au tableau, autonomie.\n'
         '5. Observer : nombres jusqu\'a 10 000, tables, techniques operatoires (grille).'),
        ('10h55-11h25', '30 min', 'Maths - Evaluation diagnostique 4 : problemes/geometrie',
         '1. Probleme 1 : 24 eleves, equipes de 4 -> combien d\'equipes ? (division)\n'
         '2. Probleme 2 : un livre 12 euros, j\'en achete 3 -> total ? (multiplication)\n'
         '3. Probleme 3 : 45 coquillages, on en donne 12 -> reste ? (soustraction)\n'
         '4. Geometrie : tracer un carre de 5 cm de cote (verifier regle, angles droits).\n'
         '5. Observer : demarche (l\'eleve ecrit-il son raisonnement ?), choix de l\'operation, soin.'),
        ('11h25-11h45', '20 min', 'Vie de classe - Presentation de l\'annee',
         '1. Montrer le calendrier scolaire de l\'annee.\n'
         '2. Presenter les cahiers (du jour, d\'entrainements) et leur usage.\n'
         '3. Lister les affaires a apporter demain (ardoise, trousse complete).\n'
         '4. Repondre aux questions.'),
        ('11h45-12h00', '15 min', 'Cloture - Bilan + mot final',
         '1. Bilan de la journee : "Qu\'est-ce qu\'on a appris ?" - 3-4 reponses.\n'
         '2. Feliciter les eleves (efforts, ecoute).\n'
         '3. Ranger la classe (chaise, table, sol).\n'
         '4. Consigne pour demain : apporter l\'ardoise + la trousse complete.\n'
         '5. Mot final bienveillant : "Demain, on continue !"'),
    ]

    for h, d, act, der in rows:
        y = pdf.get_y()
        if y > 235:
            pdf.add_page()
        # horaire + duree + activite
        pdf.set_font('Helvetica', 'B', 8)
        pdf.set_text_color(255, 255, 255)
        pdf.set_fill_color(15, 23, 42)
        pdf.cell(24, 6, h, border=1, fill=True, align='C')
        pdf.cell(13, 6, d, border=1, fill=True, align='C')
        pdf.cell(143, 6, act, border=1, fill=True)
        pdf.ln(6)
        pdf.set_font('Helvetica', '', 8.5)
        pdf.set_text_color(30, 41, 59)
        pdf.set_fill_color(248, 250, 252)
        pdf.multi_cell(180, 4.4, der, border=1, fill=True)
        pdf.ln(1.5)

    # ===== FICHE CHARTE DETAILLEE =====
    pdf.add_page()
    pdf.section('FICHE DETAILLEE : LA CHARTE DE CLASSE (30 min)')
    pdf.bullet('Objectif : construire AVEC les eleves les 5 regles de vie de la classe et le systeme de consequences.')
    pdf.bullet('Materiel : tableau, 5 affiches A4 pre-titrees (Respect, Ecoute, Parole, Travail, Securite), feutres, scotch.')
    pdf.ln(1)

    pdf.bullet('ETAPE 1 - Question de depart (5 min) :', 2)
    pdf.bullet('"Pourquoi une classe a-t-elle besoin de regles ?" Les eleves donnent leurs idees (3-5 au tableau). Reformuler : "Les regles, c\'est pour que tout le monde se sente bien et puisse travailler."', 5)

    pdf.bullet('ETAPE 2 - Echanges (10 min) :', 2)
    pdf.bullet('a) "Qu\'est-ce qui nous empeche de bien travailler ?" (le bruit, les moqueries, la violence, les objets qui trainent...)', 5)
    pdf.bullet('b) "Quelles regles pour eviter tout ca ?" - les eleves proposent des regles avec leurs mots.', 5)
    pdf.bullet('c) L\'enseignant reformule chaque proposition en phrase POSITIVE (pas de "ne pas...").', 5)

    pdf.bullet('ETAPE 3 - Synthese (10 min) :', 2)
    pdf.bullet('a) Afficher les 5 affiches au tableau, une par une. Lire chaque regle a voix haute avec la classe.', 5)
    pdf.bullet('b) Pour chaque regle, donner un exemple concret vecu le matin meme (ex : "Respect = dans le jeu des prenoms, on n\'a pas rigole quand quelqu\'un oubliait").', 5)
    pdf.bullet('c) Faire reformuler une regle par un eleve ("A ton avis, ca veut dire quoi, respecter les autres ?").', 5)

    pdf.bullet('ETAPE 4 - Consequences (5 min) :', 2)
    pdf.bullet('Expliquer le systeme en 3 temps + cas grave :', 5)
    pdf.bullet('1er avertissement : regard + rappel de la regle. | 2e fois : deplacement + discussion avec le maitre. | 3e fois : reflexion ecrite + information aux parents. | Cas grave (violence, moquerie blessante) : direction + parents.', 5)

    pdf.bullet('ETAPE 5 - Engagement (derniere minute si le temps manque, sinon apres la recreation) :', 2)
    pdf.bullet('Chaque eleve recopie la charte dans son cahier de vie et la signe ("Je m\'engage a respecter ces regles"). Afficher la charte grand format au mur, a hauteur des eleves.', 5)

    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_text_color(15, 23, 42)
    pdf.multi_cell(180, 5, 'Rappel des 5 regles (formulation positive) :')
    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(180, 4.8, '1. RESPECT : Je respecte les autres : je ne me moque pas, je n\'insulte pas.\n'
                         '2. ECOUTE : J\'ecoute quand quelqu\'un parle : le maitre ou un camarade.\n'
                         '3. PAROLE : Je leve la main et j\'attends mon tour pour parler.\n'
                         '4. TRAVAIL : Je fais mon travail avec soin et je donne le meilleur de moi.\n'
                         '5. SECURITE : Je prends soin des autres et du materiel : pas de violence, jamais.')
    pdf.ln(1)
    pdf.set_font('Helvetica', 'I', 9)
    pdf.set_text_color(100, 100, 110)
    pdf.multi_cell(180, 4.8, 'Regle d\'or : "Personne ne se moque de personne. Chacun a le droit de se tromper : c\'est comme ca qu\'on apprend."')

    out = '/workspace/periodes/cahier-journal-lundi-24-aout-2026-detaille.pdf'
    pdf.output(out)
    print(f'PDF genere : {out} ({os.path.getsize(out)} octets)')

if __name__ == '__main__':
    main()
