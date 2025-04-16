import sys
from stats import count_words, count_characters, sort_character_counts

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	path = sys.argv[1]
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")

	text = get_book_text(path)

	word_count = count_words(text)
	character_count = count_characters(text)
	sorted_characters = sort_character_counts(character_count)

	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	
	print("--------- Character Count -------")
	for item in sorted_characters:
		print(f"{item['char']}: {item['count']}")
	
	print("============= END ===============")
main()

