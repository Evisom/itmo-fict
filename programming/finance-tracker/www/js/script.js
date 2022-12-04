function request(r, callback) {
    if (r.body) {
        r.body = JSON.stringify(r.body)
    }
    fetch(r.url, {
        headers: {
            'Content-Type': 'application/json'
        },
        method: r.method, 
        body: r.body
    }).then(function(res){ 
        return res.json(); 
    }).then(function(data){ 
        callback(data); 
    })
}

window.onload = () =>{
    const container = document.getElementById("container");
    const createButton = document.getElementById('create');
    const select = document.getElementById('selectbox');
    const resetButton = document.getElementById('reset');

    function transaction(response) {
        const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
        d = new Date(response[3]).toDateString().split(' ')
        element = '<div class="transaction">\
                    <div class="tr-name">'+response[1]+'</div>\
                    <div class="tr-cost">'+response[2]+'$</div>\
                    <div class="tr-date">' + d[2]+' '+d[1]+' '+d[3] + '</div>\
                    <div class="cat">'+response[4]+'</div>\
                    <button class="deleteButton" id = "b'+response[0]+'">x</button>\
                  </div>'
        return element
    }

    function render() {
        container.innerHTML = ''
        select.innerHTML='<option>default</option>'
        request({
            url: '/getAllTransactions',
            method: 'GET',
            body: undefined
        }, (response)=> {
            console.log(response);
            for (let i = 0; i < response.length; i++) {
                container.innerHTML+=transaction(response[i])
            }
            const buttons = document.getElementsByClassName('deleteButton');
            for (let i = 0; i < buttons.length; i++) {
                buttons[i].onclick = function (el) {
                    tr_id = el.target.id.slice(1)
                    request({
                        url: '/deleteTransaction',
                        method: 'POST',
                        body: {
                            id: tr_id 
                        }}, (res)=>{
                            render()
                        })
                }
            }
        });   
        request({
            url: '/getCategories',
            method: 'GET',
            body: undefined
        }, (response) => {
            for (let i = 0; i < response.length; i++) {
                select.innerHTML+='<option id="b'+i+'">'+response[i]+'</option>'
            }
            select.onchange = () => {
                console.log(response[select.selectedIndex-1])
            }
        }) 
    }
    resetButton.onclick = ()=>{render()}

    render()
    createButton.onclick = function() {
        const data = {name: document.getElementById('name').value,
                      cost: document.getElementById('cost').value,
                      date: new Date(document.getElementById('date').value).getTime(),
                      categories: document.getElementById('categories').value}
        console.log(data)
        request({
            url: '/createTransaction',
            method: 'POST',
            body: data
        }, (response)=> {
            console.log(response);
            render()
        });
        
    }

 

}