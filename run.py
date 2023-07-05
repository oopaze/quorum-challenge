SUPPORT_VOTE_FLAG = 1
OPPOSE_VOTE_FLAG = 2


def asign_oppose_and_support_bills_count(legislators, vote_results):
    suported = []
    opposed = []

    for legislator_id in legislators["id"]:
        support_votes = vote_results[
            (vote_results["legislator_id"] == legislator_id)
            & (vote_results["vote_type"] == SUPPORT_VOTE_FLAG)
        ]

        oppose_votes = vote_results[
            (vote_results["legislator_id"] == legislator_id)
            & (vote_results["vote_type"] == OPPOSE_VOTE_FLAG)
        ]

        suported.append(len(support_votes))
        opposed.append(len(oppose_votes))

    legislators_with_votes = legislators.copy()

    legislators_with_votes["suported_bills"] = suported
    legislators_with_votes["opposed_bills"] = opposed

    return legislators_with_votes
