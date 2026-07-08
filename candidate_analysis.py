import json
import os


class CandidateAnalysis:

    def __init__(self):

        self.file_name = "candidates.json"

        self.candidates = []

        self.load_candidates()

    def load_candidates(self):

        if os.path.exists(self.file_name):

            try:

                with open(
                    self.file_name,
                    "r",
                    encoding="utf-8"
                ) as file:

                    self.candidates = json.load(file)

            except:

                self.candidates = []

    def save_candidates(self):

        with open(
            self.file_name,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.candidates,
                file,
                indent=4
            )

    def calculate_score(

        self,

        experience,

        skills,

        projects,

        communication,

        certifications

    ):

        score = 0

        score += min(experience * 8, 32)

        score += min(skills * 5, 25)

        score += min(projects * 4, 20)

        score += communication * 2

        score += certifications * 3

        return min(score, 100)

    def recommendation(self, score):

        if score >= 90:

            return "Strong Hire"

        elif score >= 75:

            return "Hire"

        elif score >= 60:

            return "Consider"

        else:

            return "Reject"

    def add_candidate(self):

        print("\n========== ADD CANDIDATE ==========\n")

        name = input("Candidate Name: ")

        role = input("Applied Role: ")

        experience = int(
            input("Experience (Years): ")
        )

        skills = int(
            input("Number of Skills: ")
        )

        projects = int(
            input("Projects Completed: ")
        )

        communication = int(
            input("Communication Rating (1-10): ")
        )

        certifications = int(
            input("Certifications: ")
        )

        score = self.calculate_score(

            experience,

            skills,

            projects,

            communication,

            certifications

        )

        candidate = {

            "name": name,

            "role": role,

            "experience": experience,

            "skills": skills,

            "projects": projects,

            "communication": communication,

            "certifications": certifications,

            "score": score,

            "recommendation": self.recommendation(score)

        }

        self.candidates.append(candidate)

        self.save_candidates()

        print("\nCandidate Added Successfully.")

    def show_candidates(self):

        if not self.candidates:

            print("\nNo Candidates Found.")

            return

        print("\n========== CANDIDATE INSIGHTS ==========\n")

        ranking = sorted(

            self.candidates,

            key=lambda x: x["score"],

            reverse=True

        )

        for index, candidate in enumerate(

            ranking,

            start=1

        ):

            print(f"Rank : {index}")

            print("Name :", candidate["name"])

            print("Role :", candidate["role"])

            print("Experience :", candidate["experience"], "Years")

            print("Skills :", candidate["skills"])

            print("Projects :", candidate["projects"])

            print("Communication :", candidate["communication"], "/10")

            print("Certifications :", candidate["certifications"])

            print("Insight Score :", candidate["score"])

            print("Recommendation :", candidate["recommendation"])

            print("-" * 50)

    def search_candidate(self):

        if not self.candidates:

            print("\nNo Candidates Found.")

            return

        keyword = input("\nCandidate Name: ").lower()

        found = False

        for candidate in self.candidates:

            if keyword in candidate["name"].lower():

                print()

                print(candidate)

                found = True

        if not found:

            print("\nCandidate Not Found.")

    def remove_candidate(self):

        if not self.candidates:

            print("\nNo Candidates Found.")

            return

        name = input("\nCandidate Name: ")

        for candidate in self.candidates:

            if candidate["name"].lower() == name.lower():

                self.candidates.remove(candidate)

                self.save_candidates()

                print("\nCandidate Removed.")

                return

        print("\nCandidate Not Found.")

    def statistics(self):

        total = len(self.candidates)

        if total == 0:

            print("\nNo Data Available.")

            return

        average = sum(

            candidate["score"]

            for candidate in self.candidates

        ) / total

        highest = max(

            candidate["score"]

            for candidate in self.candidates

        )

        lowest = min(

            candidate["score"]

            for candidate in self.candidates

        )

        print("\n========== PLATFORM STATISTICS ==========\n")

        print("Total Candidates :", total)

        print("Average Score    :", round(average, 2))

        print("Highest Score    :", highest)

        print("Lowest Score     :", lowest)