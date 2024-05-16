from utils.file_operations import read_text_file
from analyze import analyze_text
from visualize_wordcloud import generate_wordcloud_main
from visualize_distributions import generate_distributions
from summarize import summarize_text_main
from utils.cleanup import clean_outputs

def main():
    # Nettoyer le répertoire de sortie
    clean_outputs()

    # Lire le texte à partir du fichier
    text = read_text_file('data/source_text.txt')
    
    # Exécuter les analyses et visualisations
    analyze_text(text)
    generate_wordcloud_main(text)
    generate_distributions(text)
    summarize_text_main(text)

if __name__ == '__main__':
    main()
