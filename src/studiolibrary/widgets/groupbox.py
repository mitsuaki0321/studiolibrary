# Copyright 2019 by Kurt Rathjen. All Rights Reserved.
#
# This library is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. This library is distributed in the
# hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see <http://www.gnu.org/licenses/>.

import logging

from studioqt import QtCore
from studioqt import QtWidgets


logger = logging.getLogger(__name__)


class GroupBoxWidget(QtWidgets.QFrame):

    toggled = QtCore.Signal(bool)

    def __init__(self, title, widget, *args, **kwargs):
        super(GroupBoxWidget, self).__init__(*args, **kwargs)

        self._widget = None

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)

        self._titleWidget = QtWidgets.QPushButton(self)
        self._titleWidget.setCheckable(True)
        self._titleWidget.setText(title)
        self._titleWidget.setObjectName("title")
        self._titleWidget.toggled.connect(self._toggle)

        self.layout().addWidget(self._titleWidget)

        self._widgetFrame = QtWidgets.QFrame(self)
        self._widgetFrame.setObjectName("frame")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self._widgetFrame.setLayout(layout)

        self.layout().addWidget(self._widgetFrame)

        if widget:
            self.setWidget(widget)

    def setText(self, text):
        """
        Set the text to be displayed for group box.

        :type text: str
        """
        self._titleWidget.setText(text)

    def text(self):
        """
        Get the title for the group box.

        :rtype: str
        """
        return self._titleWidget.text()

    def setWidget(self, widget):
        """
        Set the widget to hide when the user clicks the title.

        :type widget: QWidgets.QWidget
        """
        self._widget = widget
        self._widget.setParent(self._widgetFrame)
        self._widgetFrame.layout().addWidget(self._widget)

    def _toggle(self, visible):
        """
        Triggered when the user clicks the title.

        :type visible: bool
        """
        self.toggled.emit(visible)

    def isChecked(self):
        """
        Check the checked state for the group box.

        :rtype: bool
        """
        return self._titleWidget.isChecked()

    def setChecked(self, checked):
        """
        Overriding this method to hide the widget when the state changes.

        :type checked: bool
        """
        self._titleWidget.setChecked(checked)
        if self._widget:
            self._widget.setVisible(checked)
