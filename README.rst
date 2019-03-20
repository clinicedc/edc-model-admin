|pypi| |travis| |codecov| |downloads|

edc-model-admin
---------------

Edc custom django ModelAdmin mixins, tags and templates


ModelAdminFormAutoNumberMixin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overrides ModelAdmin's `get_form` to insert question numbers and the DB field names.


ModelAdminNextUrlRedirectMixin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Redirects to the next CRF or Requisition listed in an edc visit schedule if "[Save and Next]"
is clicked instead of "[SAVE]"

.. code-block:: python

	class BaseModelAdmin:

	    search_fields = ("subject_identifier",)

	    add_form_template = "edc_model_admin/admin/change_form.html"
	    change_form_template = "edc_model_admin/admin/change_form.html"
	    change_list_template = "edc_model_admin/admin/change_list.html"


	@admin.register(CrfTwo)
	class CrfTwoAdmin(BaseModelAdmin, ModelAdminNextUrlRedirectMixin, admin.ModelAdmin):
	    show_save_next = True
	    show_cancel = True

You need to use the included ``change_form.html`` to override the submit buttons on the ``admin`` form.

See also:: ``edc_visit_schedule``


ModelAdminRedirectOnDeleteMixin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Redirects the admin form on save to a view other than the default ``changelist`` if ``post_url_on_delete_name`` is set. 

.. code-block:: python

	@admin.register(CrfFive)
	class CrfFiveAdmin(ModelAdminRedirectOnDeleteMixin, admin.ModelAdmin):

	    post_url_on_delete_name = "dashboard2_app:dashboard_url"

	    def post_url_on_delete_kwargs(self, request, obj):
	        return {'subject_identifier': obj.subject_identifier}





.. |pypi| image:: https://img.shields.io/pypi/v/edc-model-admin.svg
    :target: https://pypi.python.org/pypi/edc-model-admin
    
.. |travis| image:: https://travis-ci.org/clinicedc/edc-model-admin.svg?branch=develop
    :target: https://travis-ci.org/clinicedc/edc-model-admin
    
.. |codecov| image:: https://codecov.io/gh/clinicedc/edc-model-admin/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/clinicedc/edc-model-admin

.. |downloads| image:: https://pepy.tech/badge/edc-model-admin
   :target: https://pepy.tech/project/edc-model-admin
