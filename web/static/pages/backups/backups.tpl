%include('header.tpl')
<div class="content-wrapper">
<section class="content">
 <div class="box-body">
	 <div class="row">
        <div class="col-xs-12">
          <div class="box">
            <div class="box-header">
              <h3 class="box-title">últimas copias realizadas</h3>

              <div class="box-tools">
                <div class="input-group input-group-sm" style="width: 150px;">
                  <input type="text" name="table_search" class="form-control pull-right" placeholder="Search">

                  <div class="input-group-btn">
                    <button type="submit" class="btn btn-default"><i class="fa fa-search"></i></button>
                  </div>
                </div>
              </div>
            </div>
            <!-- /.box-header -->
            <div class="box-body table-responsive no-padding">
              <table class="table table-hover">
                <tr>
                  <th>Host</th>
                  <th>Fecha</th>
                  <th>Estado</th>
                  <th>Tamaño</th>
                </tr>
               
              </table>
            </div>
            <!-- /.box-body -->
          </div>
          <!-- /.box -->
</div>
</div>
        <p>
                <a class="btn bg-maroon" href="/nuevo">Nueva copia</a>
                <a class="btn bg-purple" href="/programar">Programar copia</a>
                <a class="btn bg-blue" href="/eliminar">Eliminar copia</a>
                <a class="btn bg-orange" href="/restaurar">Restaurar copia</a>
        </p>
</div>
</section>
</div>
%include('footer.tpl')
