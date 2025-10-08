import itertools

def evaluate_sentence(sentence, model):
    try:
        return eval(sentence, {}, model)
    except Exception:
        return False

def tt_entails(kb, query):
    text = " ".join(kb) + " " + query
    symbols = sorted(list(set([char for char in text if char.isupper()])))
    print(f"\nChecking if KB entails '{query}'...")
    print(f"Symbols: {symbols}")

    num_models_checked = 0
    num_kb_true = 0
    for values in itertools.product([True, False], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        kb_is_true = all(evaluate_sentence(s, model) for s in kb)
        if kb_is_true:
            num_kb_true += 1
            query_is_true = evaluate_sentence(query, model)
            print(f"  - Model {model}: KB is True. Query is {query_is_true}.")
            if not query_is_true:
                print(f"  => Entailment is FALSE. Found a counter-example.")
                return False
        num_models_checked += 1

    print(f"\nChecked {num_models_checked} models. KB was true in {num_kb_true} models.")
    if num_kb_true == 0:
        print("  => Entailment is TRUE (KB is unsatisfiable, so it entails everything).")
    else:
        print("  => Entailment is TRUE (Query was true in all models of the KB).")
    return True

if __name__ == "__main__":
    KB = [
        "(Q <= P)",
        "(P <= (not Q))",
        "(Q or R)"
    ]

    query_R = "R"
    query_R_implies_P = "(R <= P)"
    query_Q_implies_R = "(Q <= R)"

    result_1 = tt_entails(KB, query_R)
    print("-" * 30)
    result_2 = tt_entails(KB, query_R_implies_P)
    print("-" * 30)
    result_3 = tt_entails(KB, query_Q_implies_R)
    print("-" * 30)

    print("\n--- Summary of Results ---")
    print(f"Does KB entail R? {'Yes' if result_1 else 'No'}")
    print(f"Does KB entail R -> P? {'Yes' if result_2 else 'No'}")
    print(f"Does KB entail Q -> R? {'Yes' if result_3 else 'No'}")
