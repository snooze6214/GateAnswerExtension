
window.onload = () => {
    let plus_marks = 0;
    let minus_marks = 0;

    const score = (qn_no) => {
        if (qn_no >= 1 && qn_no <= 5)
            return 1;
        
        if (qn_no >= 6 && qn_no <= 10)
            return 2;
        
        if (qn_no >= 11 && qn_no <= 35)
            return 1;
        
        if (qn_no >= 36 && qn_no <= 65)
            return 2;
        
        return 0;
    }

    ans = []
    const result_rows = document.querySelectorAll('.table-hover > tbody > tr');
    result_rows.forEach(row => {
        row_vals = []
        row.childNodes.forEach(v => row_vals.push(v));
        for (let i = 0; i < 3; i++) {
            ans.push({
                qNo: Number(row_vals[3*i + 0].innerHTML),
                yourAns: row_vals[3*i + 1].innerHTML,
                qType: row_vals[3*i + 2].innerHTML
            });
        }
    });
    ans.pop();

    fetch('https://raw.githack.com/snooze6214/GateAnswerExtension/main/answers.json')
        .then(res => res.json())
        .then(data => {
            data.forEach(ele => {
                let ans_idx = ans.findIndex(e => e.qNo === ele.qNo);
                ans[ans_idx].correctAns = ele.correctAns;
                ans[ans_idx].is_correct = ans[ans_idx].correctAns === ans[ans_idx].yourAns;
                ans[ans_idx].answered = ans[ans_idx].yourAns !== '--';

                if (ans[ans_idx].is_correct === true) {
                    plus_marks += score(ans[ans_idx].qNo);
                } else {
                    if (ans[ans_idx].answered && ans[ans_idx].qType !== 'MSQ' && ans[ans_idx].qType !== 'NAT') {
                        minus_marks -= (1/3) * score(ans[ans_idx].qNo);
                    }
                }
            })
        }).then(() => {

            result_rows.forEach(row => {
                for (let i = 0; i < 3; i++) {
                    let idx = Number(row.childNodes[3*i + 0].innerHTML);
                    if (idx !== 0) {
                        if (ans[idx - 1].answered) {
                            row.childNodes[3*i + 0].style.background = (ans[idx - 1].is_correct)? 'green' : 'red';
                            row.childNodes[3*i + 1].style.background = (ans[idx - 1].is_correct)? 'green' : 'red';
                            row.childNodes[3*i + 2].style.background = (ans[idx - 1].is_correct)? 'green' : 'red';
                        }
                        if (!ans[idx - 1].is_correct) {
                            row.childNodes[3*i + 1].innerHTML += `, correct ${ans[idx - 1].correctAns}`;
                        }
                    }
                }
            });

            let above_table_text = document.getElementsByClassName('table-responsive');
            if (above_table_text[0]) {
                let mark_display = document.createElement('p');
                mark_display.textContent = `
                Correct marks : ${plus_marks},
                Incorrect marks: ${minus_marks},
                Total marks: ${plus_marks + minus_marks}
                `;
                above_table_text[0].insertAdjacentElement("beforebegin",mark_display);
            }
        });
};