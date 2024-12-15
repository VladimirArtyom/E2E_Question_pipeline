from mcq.mcq_distractor_generator import GenerateDistractorsCombineWithAllNoParaphrase
from mcq.mcq_qap_generator import GenerateQuestionAnswerPairs
from mcq.components.enums import ExperimentQG, ExperimentDG
class MCQ_Generator():
    def __init__(this,
                 qg_generator: GenerateQuestionAnswerPairs,
                 dg_generator: GenerateDistractorsCombineWithAllNoParaphrase,
                 ):
        this.qg_generator = qg_generator
        this.dg_generator = dg_generator
    
    def __call__(this, context: str,
                experiment_type_QG: ExperimentQG,
                experiment_type_DG: ExperimentDG,
                **kwargs):
        final_outputs = {}
        out_raw = []
        list_de_qag = this.qg_generator(context, experiment_type_QG, **kwargs)
        for indx, content in enumerate(list_de_qag):
            question = content[0]
            answer = content[1]
            distractors, all_outputs_raw = this.dg_generator(context, question, answer, experiment_type_DG, **kwargs)
            final_outputs[indx] = {
                "context": context,
                "question": question,
                "answer": answer,
                "distractors": distractors
            }
            out_raw.append((context, question, answer, all_outputs_raw))
        return final_outputs, out_raw