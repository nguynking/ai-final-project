from model import backtracking

def split(txt, seps=(',', ';')):
    default_sep = seps[0]

    # we skip seps[0] because that's the default separator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    num_list = [int(i.strip()) for i in txt.split(default_sep)]
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list

def main():
    demo = gr.Interface(
        fn=knapsack_backtracking, 
        inputs=[gr.Textbox(label="Set of values:"), gr.Textbox(label="Set of weights:"), gr.Textbox(label="Max weight:")], 
        outputs=[gr.Textbox(label="Total value of best set:"), gr.Textbox(label="Best set:")],
    )
        
    demo.launch()
 if __name__ == "__main__":
    main()