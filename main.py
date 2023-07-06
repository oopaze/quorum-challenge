import pandas as pd

SUPPORT_VOTE_FLAG = 1
OPPOSE_VOTE_FLAG = 2

bills = pd.read_csv("./input-files/bills.csv")
legislators = pd.read_csv("./input-files/legislators.csv")
vote_results = pd.read_csv("./input-files/vote_results.csv")
votes = pd.read_csv("./input-files/votes.csv")


def get_sponsor_name(sponsor_id, legislators=legislators):
    if sponsor_id in legislators["id"].values:
        return legislators[legislators["id"] == sponsor_id].iloc[0]["name"]
    return "Unknown"


def get_bills_votes(bills, votes, vote_results):
    suported = []
    opposed = []

    for bill_id in bills["id"]:
        if bill_id not in votes["bill_id"].values:
            continue

        vote_id = votes[votes["bill_id"] == bill_id].iloc[0]["id"]

        same_vote_id = vote_results["vote_id"] == vote_id
        is_supporting = vote_results["vote_type"] == SUPPORT_VOTE_FLAG
        is_opposing = vote_results["vote_type"] == OPPOSE_VOTE_FLAG

        support_votes = vote_results[same_vote_id & is_supporting]
        oppose_votes = vote_results[same_vote_id & is_opposing]

        suported.append(len(support_votes))
        opposed.append(len(oppose_votes))

    bills_votes = bills.copy()

    bills_votes["supporter_count"] = suported
    bills_votes["opposer_count"] = opposed
    bills_votes["primary_sponsor"] = bills_votes["sponsor_id"].apply(
        get_sponsor_name,
    )

    del bills_votes["sponsor_id"]

    return bills_votes


def asign_oppose_and_support_bills_count(legislators, vote_results):
    suported = []
    opposed = []

    for legislator_id in legislators["id"]:
        is_same_legislator = vote_results["legislator_id"] == legislator_id
        is_supporting = vote_results["vote_type"] == SUPPORT_VOTE_FLAG
        is_opposing = vote_results["vote_type"] == OPPOSE_VOTE_FLAG

        support_votes = vote_results[is_same_legislator & is_supporting]
        oppose_votes = vote_results[is_same_legislator & is_opposing]

        suported.append(len(support_votes))
        opposed.append(len(oppose_votes))

    legislators_with_votes = legislators.copy()

    legislators_with_votes["num_supported_bills"] = suported
    legislators_with_votes["num_opposed_bills"] = opposed

    return legislators_with_votes
