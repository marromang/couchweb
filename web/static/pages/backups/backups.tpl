%include('header.tpl')
<div class="content-wrapper">
<section class="content">
 <div class="box-body">
	 <div class="row">
        <div class="col-xs-12">
          <div class="box">
            <div class="box-header">
              <h3 class="box-title">Últimas copias realizadas</h3>

            </div>
            <!-- /.box-header -->
            <div class="box-body table-responsive no-padding">
              <table class="table table-hover">
<tr>
                  <th>Label-fecha</th>
                  <th>Host</th>
		  <th>Comentarios</th>
                </tr>

% for i in xrange(len(lista)):
  <tr>
	<td>{{  lista[i][0] }}</td>
        <td>{{  lista[i][1] }}</td>
        <td>{{  lista[i][4] }}</td>

  </tr>
% end		               
              </table>
            </div>
            <!-- /.box-body -->
          </div>
          <!-- /.box -->
</div>
</div>
        <p>
                <a class="btn bg-maroon" href="/nuevo">Nueva copia</a>
                <a class="btn bg-orange" href="/restaurar">Restaurar copia</a>
        </p>
</div>
</section>
</div>
%include('footer.tpl')
