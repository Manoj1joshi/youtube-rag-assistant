from datasets import Dataset
data = {
    "question": [
        question
    ],

    "answer": [
        answer
    ],

    "contexts": [
        [
            doc.page_content
            for doc in docs
        ]
    ],

    "ground_truth": [
        expected_answer
    ]
}

dataset = Dataset.from_dict(
    data
)