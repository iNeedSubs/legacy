import { mount } from '@vue/test-utils'
import LangSelect from '../../src/components/LangSelect'
import { FontAwesomeIcon } from '../../src/plugins/fa'

const defaults = {
  global: {
    components: {
      'fa': FontAwesomeIcon
    }
  }
}

describe('Language options menu', () => {
  it('is hidden by default', () => {
    const wrapper = mount(LangSelect, defaults)
    expect(wrapper.find('.options').exists()).toBeFalsy()
  })

  it('appears when clicking on button', async () => {
    const wrapper = mount(LangSelect, {
      ...defaults,
    })

    await wrapper.find('button.lang').trigger('click')
    expect(wrapper.find('.options').exists()).toBeTruthy()
  })
})
