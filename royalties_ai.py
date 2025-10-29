# ========================================
# MUSIC ROYALTIES & AI IMPACT CALCULATOR
# Version 2.0 - Enhanced Edition
# ========================================

import os
import sys

def clear_screen():
    """Clear the screen for better presentation"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Display program header"""
    print("=" * 60)
    print(" 🎵 MUSIC ROYALTIES & AI IMPACT CALCULATOR")
    print(" Simulated Future Scenario Analysis")
    print("=" * 60)
    print()

def print_menu():
    """Display main menu"""
    print("\n📋 MAIN MENU")
    print("-" * 40)
    print("1. Calculate royalties for ONE artist")
    print("2. Calculate for MULTIPLE artists (batch)")
    print("3. Compare all 3 models (Human vs AI vs Hybrid)")
    print("4. View rates and information")
    print("5. Export results to file")
    print("6. Exit")
    print("-" * 40)

def get_rates():
    """Return royalty rates"""
    return {
        'human': 0.003,
        'ai': 0.001,
        'hybrid_human': 0.0003,
        'hybrid_ai': 0.0001
    }

def calculate_royalties(streams, content_type):
    """
    Calculate royalties based on content type
    
    Arguments:
        streams (int): Number of streams
        content_type (str): 'human', 'ai', or 'hybrid'
    
    Returns:
        dict: Calculated royalty details
    """
    rates = get_rates()
    
    if content_type == 'human':
        total = streams * rates['human']
        return {
            'type': 'Human Only',
            'streams': streams,
            'human_share': total,
            'ai_share': 0,
            'total': total,
            'rate': rates['human']
        }
    
    elif content_type == 'ai':
        total = streams * rates['ai']
        return {
            'type': 'AI Only',
            'streams': streams,
            'human_share': 0,
            'ai_share': total,
            'total': total,
            'rate': rates['ai']
        }
    
    elif content_type == 'hybrid':
        human_share = streams * rates['hybrid_human']
        ai_share = streams * rates['hybrid_ai']
        total = human_share + ai_share
        return {
            'type': 'Hybrid (Human + AI)',
            'streams': streams,
            'human_share': human_share,
            'ai_share': ai_share,
            'total': total,
            'rate': rates['hybrid_human'] + rates['hybrid_ai']
        }

def print_results(results):
    """Display results in formatted way"""
    print("\n" + "=" * 60)
    print(" 📊 CALCULATION RESULTS")
    print("=" * 60)
    print(f"\n🎵 Content Type       : {results['type']}")
    print(f"📈 Number of Streams  : {results['streams']:,}")
    print(f"💵 Rate per Stream    : ${results['rate']:.6f}")
    print()
    print("-" * 60)
    
    if results['human_share'] > 0:
        print(f"👤 Human Artist Share   : ${results['human_share']:,.2f}")
    
    if results['ai_share'] > 0:
        print(f"🤖 AI Provider Share    : ${results['ai_share']:,.2f}")
    
    print("-" * 60)
    print(f"💰 TOTAL ROYALTIES      : ${results['total']:,.2f}")
    print("=" * 60)

def single_calculation():
    """Mode 1: Calculate for single artist"""
    clear_screen()
    print_header()
    print("\n📝 MODE: Single Calculation\n")
    
    # Ask for number of streams
    while True:
        try:
            streams = int(input("📈 Enter number of streams: "))
            if streams <= 0:
                print("❌ Error: Number must be positive!")
                continue
            break
        except ValueError:
            print("❌ Error: Please enter a valid number!")
    
    # Ask for content type
    print("\n🎯 Choose content type:")
    print("   1. Human Only (Human artist)")
    print("   2. AI Only (AI-generated)")
    print("   3. Hybrid (Human + AI)")
    
    while True:
        choice = input("\nYour choice (1/2/3): ").strip()
        if choice == '1':
            content_type = 'human'
            break
        elif choice == '2':
            content_type = 'ai'
            break
        elif choice == '3':
            content_type = 'hybrid'
            break
        else:
            print("❌ Invalid choice! Choose 1, 2 or 3.")
    
    # Calculate and display
    results = calculate_royalties(streams, content_type)
    print_results(results)
    
    input("\n⏎ Press Enter to continue...")

def batch_calculation():
    """Mode 2: Calculate for multiple artists"""
    clear_screen()
    print_header()
    print("\n📝 MODE: Batch Calculation\n")
    
    artists = []
    
    while True:
        print(f"\n👤 Artist #{len(artists) + 1}")
        print("-" * 40)
        
        # Artist name
        name = input("Artist name (or 'done' to finish): ").strip()
        
        if name.lower() == 'done':
            if len(artists) == 0:
                print("⚠️  You must enter at least one artist!")
                continue
            break
        
        # Streams
        while True:
            try:
                streams = int(input("Number of streams: "))
                if streams <= 0:
                    print("❌ Number must be positive!")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number!")
        
        # Type
        print("\nContent type:")
        print("  1. Human Only")
        print("  2. AI Only")
        print("  3. Hybrid (Human + AI)")
        
        while True:
            choice = input("Choice (1/2/3): ").strip()
            if choice == '1':
                content_type = 'human'
                break
            elif choice == '2':
                content_type = 'ai'
                break
            elif choice == '3':
                content_type = 'hybrid'
                break
            else:
                print("❌ Invalid choice!")
        
        # Calculate and add
        results = calculate_royalties(streams, content_type)
        results['name'] = name
        artists.append(results)
        
        print(f"✅ {name} added!")
    
    # Display summary table
    print("\n" + "=" * 80)
    print(" 📊 ROYALTIES SUMMARY")
    print("=" * 80)
    print(f"{'Artist':<20} {'Type':<20} {'Streams':>15} {'Royalties':>15}")
    print("-" * 80)
    
    total_streams = 0
    total_royalties = 0
    
    for artist in artists:
        print(f"{artist['name']:<20} {artist['type']:<20} {artist['streams']:>15,} ${artist['total']:>14,.2f}")
        total_streams += artist['streams']
        total_royalties += artist['total']
    
    print("-" * 80)
    print(f"{'TOTAL':<20} {'':<20} {total_streams:>15,} ${total_royalties:>14,.2f}")
    print("=" * 80)
    
    input("\n⏎ Press Enter to continue...")
    
    # Ask if user wants to export
    export = input("\n💾 Export these results to file? (y/n): ").strip().lower()
    if export == 'y':
        export_results(artists)

def comparison_mode():
    """Mode 3: Compare all 3 models"""
    clear_screen()
    print_header()
    print("\n📊 MODE: Model Comparison\n")
    
    while True:
        try:
            streams = int(input("📈 Enter number of streams to compare: "))
            if streams <= 0:
                print("❌ Number must be positive!")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Calculate for all 3 models
    human_results = calculate_royalties(streams, 'human')
    ai_results = calculate_royalties(streams, 'ai')
    hybrid_results = calculate_royalties(streams, 'hybrid')
    
    # Display comparison
    print("\n" + "=" * 80)
    print(" 🔄 COMPARISON OF 3 MODELS")
    print("=" * 80)
    print(f"\n📈 Number of streams: {streams:,}\n")
    print(f"{'Model':<25} {'Rate/Stream':<15} {'Total Royalties':<20} {'Difference':<15}")
    print("-" * 80)
    
    max_royalty = human_results['total']
    
    print(f"{'👤 Human Only':<25} ${human_results['rate']:<14.6f} ${human_results['total']:<19,.2f} {'(BASE)':<15}")
    
    ai_diff = ((ai_results['total'] - max_royalty) / max_royalty) * 100
    print(f"{'🤖 AI Only':<25} ${ai_results['rate']:<14.6f} ${ai_results['total']:<19,.2f} {ai_diff:>+.1f}%")
    
    hybrid_diff = ((hybrid_results['total'] - max_royalty) / max_royalty) * 100
    print(f"{'🔄 Hybrid (H+AI)':<25} ${hybrid_results['rate']:<14.6f} ${hybrid_results['total']:<19,.2f} {hybrid_diff:>+.1f}%")
    
    print("=" * 80)
    
    # Insights
    print("\n💡 INSIGHTS:")
    print(f"   • Human model generates {human_results['total'] / ai_results['total']:.1f}x more royalties than AI Only")
    print(f"   • Hybrid model generates {hybrid_results['total'] / ai_results['total']:.1f}x more than AI Only")
    print(f"   • Artists lose {100 - (ai_results['total'] / human_results['total'] * 100):.1f}% with AI Only vs Human Only")
    
    input("\n⏎ Press Enter to continue...")

def show_info():
    """Mode 4: Display rate information"""
    clear_screen()
    print_header()
    print("\n📚 RATE INFORMATION\n")
    
    rates = get_rates()
    
    print("=" * 60)
    print(" 💵 ROYALTY RATES PER STREAM")
    print("=" * 60)
    print(f"\n👤 Human Only          : ${rates['human']:.6f} per stream")
    print(f"🤖 AI Only             : ${rates['ai']:.6f} per stream")
    print(f"🔄 Hybrid - Human Part : ${rates['hybrid_human']:.6f} per stream")
    print(f"🔄 Hybrid - AI Part    : ${rates['hybrid_ai']:.6f} per stream")
    print(f"🔄 Hybrid - TOTAL      : ${rates['hybrid_human'] + rates['hybrid_ai']:.6f} per stream")
    print("=" * 60)
    
    print("\n📖 CONCRETE EXAMPLE:")
    print("-" * 60)
    print("For 1,000,000 streams:")
    print(f"  • Human Only  → ${1000000 * rates['human']:,.2f}")
    print(f"  • AI Only     → ${1000000 * rates['ai']:,.2f}")
    print(f"  • Hybrid      → ${1000000 * (rates['hybrid_human'] + rates['hybrid_ai']):,.2f}")
    print(f"                   └─ Artist: ${1000000 * rates['hybrid_human']:,.2f}")
    print(f"                   └─ AI Provider: ${1000000 * rates['hybrid_ai']:,.2f}")
    
    print("\n⚠️  DISCLAIMER:")
    print("All data is SIMULATED for demonstration purposes.")
    print("This project explores future scenarios for the music industry.")
    
    input("\n⏎ Press Enter to continue...")

def export_results(artists):
    """Export results to text file"""
    filename = input("\n📝 Filename (without extension): ").strip()
    if not filename:
        filename = "royalties_results"
    
    filename = filename + ".txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write(" MUSIC ROYALTIES CALCULATION RESULTS\n")
            f.write(" Generated by Music Royalties & AI Calculator v2.0\n")
            f.write("=" * 80 + "\n\n")
            
            f.write(f"{'Artist':<20} {'Type':<20} {'Streams':>15} {'Royalties':>15}\n")
            f.write("-" * 80 + "\n")
            
            total_streams = 0
            total_royalties = 0
            
            for artist in artists:
                f.write(f"{artist['name']:<20} {artist['type']:<20} {artist['streams']:>15,} ${artist['total']:>14,.2f}\n")
                total_streams += artist['streams']
                total_royalties += artist['total']
            
            f.write("-" * 80 + "\n")
            f.write(f"{'TOTAL':<20} {'':<20} {total_streams:>15,} ${total_royalties:>14,.2f}\n")
            f.write("=" * 80 + "\n\n")
            
            f.write("⚠️  DISCLAIMER:\n")
            f.write("All data is simulated for demonstration purposes.\n")
            f.write("This project explores potential future scenarios for the music industry.\n")
        
        print(f"\n✅ Results successfully exported to '{filename}'!")
    except Exception as e:
        print(f"\n❌ Error during export: {e}")

def main():
    """Main program function"""
    while True:
        clear_screen()
        print_header()
        print_menu()
        
        choice = input("\n👉 Your choice: ").strip()
        
        if choice == '1':
            single_calculation()
        elif choice == '2':
            batch_calculation()
        elif choice == '3':
            comparison_mode()
        elif choice == '4':
            show_info()
        elif choice == '5':
            print("\n⚠️  Use mode 2 (Batch) to export results.")
            input("⏎ Press Enter to continue...")
        elif choice == '6':
            clear_screen()
            print("\n" + "=" * 60)
            print(" 👋 Thank you for using the Royalties Calculator!")
            print(" Project created by: Prudent Honliasso")
            print(" Contact: prudenthonliasso@gmail.com")
            print("=" * 60 + "\n")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice! Choose between 1 and 6.")
            input("⏎ Press Enter to continue...")

# Program entry point
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user.")
        print("Goodbye! 👋\n")
        sys.exit(0)
