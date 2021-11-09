import Graphics.UI.Gtk
main = do
         initGUI
         dialog <- messageDialogNew Nothing [DialogModal] MessageInfo ButtonsOk "Hello world!"
         messageDialogSetSecondaryText dialog "This is an example dialog."
         _res <- dialogRun dialog
         return 0
