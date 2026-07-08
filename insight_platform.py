from candidate_analysis import CandidateAnalysis


class CandidateInsightPlatform:

    def __init__(self):

        self.analysis = CandidateAnalysis()

    def display_menu(self):

        while True:

            print("\n")

            print("=" * 55)

            print("         CANDIDATE INSIGHT PLATFORM")

            print("=" * 55)

            print("1. Add Candidate")

            print("2. View Candidate Insights")

            print("3. Search Candidate")

            print("4. Remove Candidate")

            print("5. Platform Statistics")

            print("6. Exit")

            choice = input("\nEnter Choice: ").strip()

            if choice == "1":

                try:

                    self.analysis.add_candidate()

                except ValueError:

                    print("\nInvalid Input.")

            elif choice == "2":

                self.analysis.show_candidates()

            elif choice == "3":

                self.analysis.search_candidate()

            elif choice == "4":

                self.analysis.remove_candidate()

            elif choice == "5":

                self.analysis.statistics()

            elif choice == "6":

                print("\nThank You For Using Candidate Insight Platform!")

                break

            else:

                print("\nInvalid Choice.")


if __name__ == "__main__":

    platform = CandidateInsightPlatform()

    platform.display_menu()