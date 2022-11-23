        // SCRIPT DE UPDATE CLICANDO NA TABELA
        $(document).ready(function(){
            $(document).on("dblclick",".editable",function(){
                var value=$(this).text();
                var data_type=$(this).data("type");
                var input_type="text";
                if(data_type=="created_at")
                {
                    input_type="datetime-local";
                }
                var input="<input type='"+input_type+"' class='input-data' value='"+value+"' class='form-control'>";
                $(this).html(input);
                $(this).removeClass("editable")
            });

            $(document).on("blur",".input-data",function(){
                var value=$(this).val();
                var td=$(this).parent("td");
                $(this).remove();
                td.html(value);
                td.addClass("editable");
                var type=td.data("type");
                sendToServer(td.data("id"),value,type);
            });
            $(document).on("keypress",".input-data",function(e){
                var key=e.which;
                if(key==13){
                    var value=$(this).val();
                    var td=$(this).parent("td");
                    $(this).remove();
                    td.html(value);
                    td.addClass("editable");
                   var type=td.data("type");
                   sendToServer(td.data("id"),value,type);
                }
            });

            function sendToServer(id,value,type){
                console.log(id);
                console.log(value);
                console.log(type);
                $.ajax({
                    url:"http://127.0.0.1:8000/app/empresa/save",
                    type:"POST",
                    data:{id:id,type:type,value:value},
                })
                .done(function(response){
                    console.log(response);
                })
                .fail(function(){
                   console.log("Error Occured");
                });

            }
        });

        // SCRIPT DE INSERT
        $(".btn-insert-data").click(function(){
            var select = document.getElementById("id_cod_projeto");
            var cod_projeto = select.options[select.selectedIndex].text;
            var opcaoValor = select.options[select.selectedIndex].value;
            var empresa=$("#id_empresa").val();
            var safegold_ger=$("#id_safegold_ger").val();
            var cnpj=$("#id_cnpj").val();
            var data_cadastro= new Date().toLocaleDateString(undefined, {year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', hour12: false, minute:'2-digit'});
            var data_atualiza= new Date().toLocaleDateString(undefined, {year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', hour12: false, minute:'2-digit'});
            console.log(data_cadastro, safegold_ger)
            if(empresa==""){
                $("#ins_error").text("Digite o nome da empresa")
                $("#ins_error").show()
                return;
            }

            else if(cnpj.length != 14){
                $("#ins_error").text("CNPJ INVALIDO")
                $("#ins_error").show()
                return;
            }
            else{
                $.ajax({
                    url:"{% url 'crud_app:insert' %}",
                    type:'POST',
                    data:{cod_projeto:opcaoValor,empresa:empresa,safegold_ger:safegold_ger,cnpj:cnpj}
                })
                .done(function(response){
                    if(response['error']==false){
                        $("#ins_error").hide();
                        $("#ins_success").text(response['errorMessage']);
                        $("#ins_success").show();
                        var html_data="<tr><td class='text-center col-md-1'>"+response['cod_empresa']+"</td><td class='editable' data-type='empresa'>"+empresa+"</td><td class='editable' data-type='empresa'>"+cod_projeto+"</td><td>"+data_cadastro+"</td><td>"+data_atualiza+"</td><td class='editable' data-type='cnpj'>"+cnpj+"</td><td class='ignore-on-print excludeExport text-center col-md-2'><a href='/app/empresa/detail/"+response['cod_empresa']+"/' class='mx-3' title='Detalhar Conta'><i class='fa-solid fa-up-right-and-down-left-from-center'></i></a><a href='/app/empresa/delete/"+response['cod_empresa']+"/' class='mx-3' title='Excluir Conta'><i class='fa-solid fa-trash-can'></i></a></td>";
                        $(".table tbody").prepend(html_data);
                                        
                    }
                    else{
                        $("#ins_success").hide();
                        $("#ins_error").text(response['errorMessage']);
                        $("#ins_error").show();
                    }
                })
                .fail(function(){
                    $("#ins_success").hide();
                    $("#ins_error").text("Something Went Wrong!");
                    $("#ins_error").show();
               })
               .always(function(){
                   $(".btn-insert-data").removeAttr("disabled");
                   $(".btn-insert-data").text("INSERT EMPRESAS");
               })
           }
       });
       // SCRIPT DE DELETE
       $(document).on("click",".btn-delete",function(){
        var this_html=$(this);
        this_html.attr("disabled","disabled");
        this_html.text("DELETING....");
        var cod_empresa=this_html.parent().parent().children().first().text();
        //console.log(id);
        $.ajax({
            url:"#",
            type:'POST',
            data:{cod_empresa:cod_empresa}
        })
        .done(function(response){
            if(response['error']==false){
                this_html.parent().parent().remove();
                $("#upt_error").hide();
                $("#upt_success").text(response['errorMessage']);
                $("#upt_success").show();

            }
            else{
                $("#upt_success").hide();
                $("#upt_error").text(response['errorMessage']);
                $("#upt_error").show();
            }
        })
        .fail(function(){
             $("#upt_success").hide();
             $("#upt_error").text("Something Went Wrong!");
             $("#upt_error").show();
        });
});
 
    // SCRIPT DE UPDATE ALL 
$("#update_btn").click(function(){
    $("#update_btn").hide();
    $("#save_all_btn").show();

$(".editable").each(function(){
   var value=$(this).text();
   var types=$(this).data('type');

    var html_data="<input type='text' name='"+types+"'  class='form-control input_"+types+" input_data' value='"+value+"'>";
    $(this).html(html_data);

});
});

$("#save_all_btn").click(function(){
$("#save_all_btn").attr("disabled","disabled");
$("#save_all_btn").text("Saving Data....");

var json_data=[];
$(".input_data").each(function(){
        var value=$(this).val();
        var parent_html=$(this).parent();
        parent_html.html(value);
        $(this).remove();
 });
$("tbody tr").each(function(){
     var cod_empresa=$(this).children().eq(0).text()
     var empresa=$(this).children().eq(1).text()
     var cnpj=$(this).children().eq(5).text()
    console.log(cod_empresa)
    console.log(empresa)
    console.log(cnpj)
     var single_data={"cod_empresa":cod_empresa,"empresa":empresa,"cnpj":cnpj};
     json_data.push(single_data);
});
console.log(json_data)

var string_data=JSON.stringify(json_data)
$.ajax({
        url:'{% url 'crud_app:update_all' %}',
        type:'POST',
        data:{data:string_data}
    })
    .done(function(response){
        if(response['error']==false){
            $("#upt_error").hide();
            $("#upt_success").text(response['errorMessage']);
            $("#upt_success").show();

        }
        else{
            $("#upt_success").hide();
            $("#upt_error").text(response['errorMessage']);
            $("#upt_error").show();
        }
    })
    .fail(function(){
         $("#upt_success").hide();
         $("#upt_error").text("Something Went Wrong!");
         $("#upt_error").show();
    })
    .always(function(){
         $("#save_all_btn").removeAttr("disabled");
         $("#save_all_btn").text("SAVE ALL");
         $("#update_btn").show();
         $("#save_all_btn").hide();
    })

});


