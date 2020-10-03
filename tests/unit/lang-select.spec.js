import { mount } from '@vue/test-utils'
import LangSelect from '../../src/components/LangSelect'
import { LangCode, LangName } from '../../src/ts/languages'
import { FontAwesomeIcon } from '../../src/plugins/fa'

const defaults = {
  global: {
    components: {
      'fa': FontAwesomeIcon
    }
  }
}

describe('Language Selection', () => {
  describe('Button', () => {
    it('shows correct language after selection', async () => {
      const wrapper = mount(LangSelect, defaults)
      await wrapper.vm.setLang(LangCode.RUSSIAN)
      expect(wrapper.find('button.lang').text()).toBe(LangName.RUS)
    })

    it('emits lang-update event once with the new lang code', async () => {
      const wrapper = mount(LangSelect, defaults)
      await wrapper.vm.setLang(LangCode.RUSSIAN)

      expect(wrapper.emitted('update-lang')).toBeTruthy()
      expect(wrapper.emitted('update-lang').length).toBe(1)
      expect(wrapper.emitted('update-lang')[0]).toEqual(['rus'])
    })
  })

  describe('Menu', () => {
    it('is hidden by default', () => {
      const wrapper = mount(LangSelect, defaults)
      expect(wrapper.find('.options').exists()).toBeFalsy()
    })

    it('appears when clicking on button', async () => {
      const wrapper = mount(LangSelect, defaults)
      await wrapper.find('button.lang').trigger('click')
      expect(wrapper.find('.options').exists()).toBeTruthy()
    })
  })
})
