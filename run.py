from main import asign_oppose_and_support_bills_count, get_bills_votes


if __name__ == "__main__":
    legislators_with_votes = asign_oppose_and_support_bills_count()
    bills_with_votes = get_bills_votes()

    legislators_with_votes.to_csv(
        "output-files/legislators-support-oppose-count.csv",
        index=False,
    )
    bills_with_votes.to_csv("output-files/bills.csv", index=False)
