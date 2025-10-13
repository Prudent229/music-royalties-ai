# royalties_ai.py

def calculate_royalties(streams, rate):
    return streams * rate

print(" Welcome to the Music Royalties Simulator")

streams = int(input("Enter number of streams: "))
content_type = input("Was this music AI-generated? (yes/no): ").lower()

# Hypothetical rates
human_rate = 0.003
ai_rate = 0.001

if content_type == "yes":
    rate = ai_rate
    origin = "AI-generated"
else:
    rate = human_rate
    origin = "Human artist"

royalties = calculate_royalties(streams, rate)

print(f"\nType: {origin}")
print(f"Rate applied: ${rate}")
print(f"Estimated Royalties: ${royalties:.2f}")
