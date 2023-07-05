SUPPORT_VOTE_FLAG = 1
OPPOSE_VOTE_FLAG = 2


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
