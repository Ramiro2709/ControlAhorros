$(function(){

    $("#select_tipo").on('change', function () {
        id_tipo = $(this).val();
        console.log("Id tipo: "+id_tipo);

        desc =  $("#id_descripcion");
        cat_or =  $("#id_categoria_origen");
        subcat_or =  $("#id_subcat_origen");
        cat_dest =  $("#id_categoria_dest");
        subcat_dest =  $("#id_subcat_dest");
        moneda_origen =  $("#id_moneda_origen");
        monto_origen =  $("#id_monto_origen");
        plataforma_or =  $("#id_plataforma_or");
        plataforma_des =  $("#id_plataforma_des");
    

        //NOTE Depende el tipo de registro, pone valores predeterminados
        switch(id_tipo){
            case "1":{
                // Ingreso de Sueldo
                // Categoria: Ingresos 3 , Sub: Sueldo (4) , dest: Ingresos 3, sub, Cartera (5)
                // Moneda Origen: ARS (1), Monto Origen 30000 , Plat or: SantaCruz (2), , plat dest MercadoPago
                console.log("Ingreso de Sueldo");
                desc.val("Ingreso de Sueldo") ;
                cat_or.val(3);
                subcat_or.val(4);
                cat_dest.val(3);
                subcat_dest.val(5);
                moneda_origen.val(1);
                monto_origen.val(30000);
                plataforma_or.val(2);
                plataforma_des.val(1);
                break;
            }
            case "5":{
                // Cambiar Categoria
                // Pone: Desc: "Transferencia de categoria: ..." ,
                // Categoria: Ingresos 3, sub, Cartera (5) , dest: Inversiones 4, sub, Distribucion (11)
                // Moneda Origen: ARS (1), Monto Origen 2000 , Plat or: MercadoPago (1), , plat dest MercadoPago
                console.log("Cambiar");
                desc.val("Transferencia de categoria: ...") ;
                cat_or.val(3);
                subcat_or.val(5);
                cat_dest.val(4);
                subcat_dest.val(11);
                moneda_origen.val(1);
                monto_origen.val(7000);
                plataforma_or.val(1);
                plataforma_des.val(1);
                break;
            }
            case "6":{
                // A binance P2P
                // Pone: Desc: "Comprados BUSD en Binance por P2P" ,
                // Categoria: Inversiones 4 , Sub: Distribucion (11) , dest: Inversiones 4, sub, Distribucion (11)
                // Moneda Origen: ARS (1), Monto Origen 2000 , Plat or: ,MercadoPago , plat dest Binance (3)
                console.log("P2P");
                desc.val("Comprados BUSD en Binance por P2P") ;
                cat_or.val(4);
                subcat_or.val(11);
                cat_dest.val(4);
                subcat_dest.val(11);
                moneda_origen.val(1);
                monto_origen.val(2000);
                plataforma_or.val(1);
                plataforma_des.val(3);
                break;
            }
            default:
                console.log("Default");
                
        }
    });

    /*
    function mostrar_contenido(bloque){
        console.log("test")
        $("#content").find('.active').hide();
        $("#content").find('.active').removeClass('active');

        $(bloque).addClass('active');
        $(bloque).show(); 
    }
    */

});
